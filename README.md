# MCP_AICallAssistant

# 🤖 AI Calling Assistant using Model Context Protocol (MCP)

Ever wanted to call your AI and have it talk back — with memory, voice, and actual intelligence?

This project is a plug-and-play **MCP-based AI voice assistant** that picks up your phone call, understands what you're saying, responds with GPT-4, and talks back — all in real time.

> 🧠 Built using Model Context Protocol (MCP) — to structure the input, memory, model reasoning, and output.

---

## 📞 What It Does

- Receives a **phone call** via Twilio  
- Transcribes user speech to text  
- Passes conversation to **MCP server** with context  
- **GPT-4** generates a reply based on prior memory  
- Sends the reply back as **speech** using ElevenLabs (or just text)  
- Waits for more input and repeats 🔁

You can literally have a full conversation with your AI — like it’s your personal assistant.

---

## 🧠 What is MCP?

**Model Context Protocol** (MCP) is a framework to build modular AI agents. It separates:

- 🗣 **Input** (e.g., voice, chat, sensors)  
- 🧠 **Memory/Context** (stored over time)  
- 🤖 **Model** (e.g., GPT-4, Claude, local LLMs)  
- 📤 **Output** (text, speech, UI action, etc)

This architecture makes it easy to build scalable, pluggable agents across different interfaces — like phone calls, web chat, or even apps.

---

## 🛠 Tech Stack

- **Python** (Flask for MCP server)
- **OpenAI GPT-4** (for conversational logic)
- **Twilio Programmable Voice** (for receiving phone calls + transcription)
- **ElevenLabs API** (optional, for lifelike voice replies)
- **ngrok** (for local testing over HTTPS)

---
