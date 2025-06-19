import requests
import uuid
import os

ELEVEN_API_KEY = ""
VOICE_ID =  "EXAVITQu4vr4xnSDxMaL"  # Default voice

def text_to_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    print("\n--- ElevenLabs Request ---")
    print("POST", url)
    print("Headers:", headers)
    print("Payload:", payload)

    response = requests.post(url, headers=headers, json=payload)

    print("\n--- ElevenLabs Response ---")
    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("Response text:", response.text)
        raise Exception("❌ ElevenLabs failed to synthesize speech")

    filename = f"speech_{uuid.uuid4()}.wav"
    with open(filename, "wb") as f:
        f.write(response.content)

    print("✅ Audio file saved at:", filename)
    return filename