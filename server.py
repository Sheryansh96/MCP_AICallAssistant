# === FILE: server.py ===
# Main MCP server entrypoint
from flask import Flask, request, send_file, jsonify, Response
from mcp_core.context import get_memory_for_user
from mcp_core.llm_handler import generate_reply
from mcp_core.tts import text_to_speech
from twilio.twiml.voice_response import VoiceResponse, Gather
import uuid
import os

app = Flask(__name__)

# @app.before_request
# def log_request():
#     print(f"Incoming {request.method} request to {request.path}")
#     print(f"Form data: {request.form.to_dict()}")

# @app.route("/")
# def root():
#     print("✅ Root endpoint hit")
#     return "MCP server is up"

@app.route("/mcp/message", methods=["POST"])
def mcp_message():
    data = request.get_json()
    print("Received data:", data)

    memory_id = data.get("memory_id")
    messages = data.get("messages")
    output_type = data.get("output", "text")

    if not memory_id or not messages:
        return jsonify({"error": "Missing memory_id or messages"}), 400

    memory = get_memory_for_user(memory_id)
    memory.extend(messages)
    print("Memory after extend:", memory)

    reply = generate_reply(memory)
    print("Generated reply:", reply)
    memory.append({"role": "assistant", "content": reply})

    if output_type == "audio":
        print("🟡 AUDIO mode triggered — calling text_to_speech()")
        audio_path = text_to_speech(reply)
        print("🟢 Audio file generated at:", audio_path)
        return send_file(audio_path, mimetype="audio/wav")

    else:
        return jsonify({"reply": reply})

@app.route("/", methods=['POST'])
def twilio_voice():
    memory = get_memory_for_user("twilio-user")
    user_input = request.form.get("SpeechResult")

    if user_input:
        print(f"🗣️ User said: {user_input}")
        memory.append({"role": "user", "content": user_input})
        reply = generate_reply(memory)
        memory.append({"role": "assistant", "content": reply})
    else:
        reply = "Hello! How can I help you today?"

    print(f"🤖 GPT reply: {reply}")

    # Create Twilio voice response
    vr = VoiceResponse()
    vr.say(reply, voice='Polly.Amy', language='en-GB')

    # 👇 Add a <Gather> so user can reply again
    gather = Gather(
        input='speech',
        action='/',
        method='POST',
        timeout=5
    )
    gather.say("You can speak after the beep.", voice='Polly.Amy')
    vr.append(gather)

    return Response(str(vr), mimetype="application/xml")



if __name__ == "__main__":
    app.run(port=5050)