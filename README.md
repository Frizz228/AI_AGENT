# 🤖 My AI Agent

A simple yet powerful AI agent built with **OpenAI GPT-4o-mini** and **Python**.
The agent can reason, call tools, and remember the conversation — and it always
replies in **English**, regardless of the language you write in.

---

## ✨ Features

- 🧠 **LLM-powered reasoning** — uses OpenAI's function-calling API
- 🔧 **Tool use** — the agent decides when to call external functions
- 💬 **Conversation memory** — remembers context across turns
- 🌍 **English-only replies** — always answers in English
- 🖥️ **Simple CLI** — runs in your terminal
- ⚡ **Minimal dependencies** — just `openai` + `python-dotenv`

### Built-in tools

| Tool | Description |
|------|-------------|
| `get_current_time` | Returns the current date and time |
| `calculate` | Evaluates safe math expressions (e.g. `sqrt(16)+2`) |
| `get_weather` | Returns weather for a city (demo data) |
| `save_note` | Saves a note to a local `.txt` file |

---

## 📁 Project structure
