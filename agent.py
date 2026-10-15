# agent.py
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from tools import TOOLS_SCHEMA, AVAILABLE_FUNCTIONS

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY", "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")
client = OpenAI(api_key=API_KEY)

MODEL = "gpt-4o-mini"

# 👇 The system prompt forces English-only replies
SYSTEM_PROMPT = (
    "You are a smart AI agent. "
    "ALWAYS respond in English, no matter what language the user writes in. "
    "Use the available tools whenever they help. "
    "Keep answers short, clear and to the point."
)

# Conversation memory
messages = [{"role": "system", "content": SYSTEM_PROMPT}]


def run_agent(user_input: str, max_iterations: int = 5, verbose: bool = True) -> str:
    """Runs one turn of the agent loop."""
    messages.append({"role": "user", "content": user_input})

    for _ in range(max_iterations):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS_SCHEMA,
            tool_choice="auto",
        )
        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)

            for call in msg.tool_calls:
                fn_name = call.function.name
                fn_args = json.loads(call.function.arguments or "{}")

                if verbose:
                    print(f"  🔧 Call: {fn_name}({fn_args})")

                fn = AVAILABLE_FUNCTIONS.get(fn_name)
                if fn is None:
                    result = f"Tool {fn_name} not found"
                else:
                    try:
                        result = fn(**fn_args)
                    except Exception as e:
                        result = f"Tool error: {e}"

                if verbose:
                    print(f"  📤 Result: {result}")

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result),
                })
            continue

        messages.append(msg)
        return msg.content or "(empty reply)"

    return "⚠️ Step limit reached, the agent could not finish the task."


def reset_memory():
    """Clears conversation history."""
    global messages
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]


# --- CLI ---
if __name__ == "__main__":
    print("🤖 AI agent started. Type 'exit' to quit, 'reset' to clear memory.\n")
    while True:
        try:
            user = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break

        if not user:
            continue
        if user.lower() in ("exit", "quit"):
            print("Bye!")
            break
        if user.lower() == "reset":
            reset_memory()
            print("🧹 Memory cleared.\n")
            continue

        print("Agent is thinking...")
        answer = run_agent(user)
        print(f"\n🤖 Agent: {answer}\n")