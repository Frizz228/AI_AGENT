# tools.py
import math
import datetime


def get_current_time() -> str:
    """Returns the current date and time."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def calculate(expression: str) -> str:
    """Evaluates a math expression. Example: '2+2*10'."""
    try:
        allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        allowed["abs"] = abs
        allowed["round"] = round
        result = eval(expression, {"__builtins__": {}}, allowed)
        return str(result)
    except Exception as e:
        return f"Calculation error: {e}"


def get_weather(city: str) -> str:
    """Fake weather. Replace with a real API (OpenWeatherMap) later."""
    fake_data = {
        "moscow": "+5°C, cloudy",
        "london": "+8°C, foggy",
        "new york": "+12°C, sunny",
        "tokyo": "+16°C, clear",
    }
    key = city.lower().strip()
    return fake_data.get(key, f"No data for {city}. (demo)")


def save_note(filename: str, content: str) -> str:
    """Saves a note to a file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Note saved to {filename}"
    except Exception as e:
        return f"Error: {e}"


# --- OpenAI tool schemas ---
TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current date and time",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Example: '2+2*10' or 'sqrt(16)'",
                    }
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather in a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "save_note",
            "description": "Save a note to a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["filename", "content"],
            },
        },
    },
]

AVAILABLE_FUNCTIONS = {
    "get_current_time": get_current_time,
    "calculate": calculate,
    "get_weather": get_weather,
    "save_note": save_note,
}