import webbrowser
from datetime import datetime
import re

def show_time():
    now = datetime.now()
    print("🕒 Current time:", now.strftime("%I:%M:%S %p"))

def open_website(command: str):
    # Built-in shortcuts
    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "wikipedia": "https://www.wikipedia.org",
        "linkedin": "https://www.linkedin.com",
    }

    # Examples supported:
    #   open google
    #   open https://example.com
    #   open example.com
    parts = command.split(maxsplit=1)
    if len(parts) < 2:
        print("Usage: open <site-name|url> (e.g., open google OR open https://example.com)")
        return

    target = parts[1].strip().lower()

    if target in sites:
        url = sites[target]
    else:
        # If user typed a domain without scheme, add https://
        url = target
        if not re.match(r"^https?://", url):
            url = "https://" + url

    webbrowser.open(url, new=2)
    print(f"🌐 Opening: {url}")

def safe_calculate(expr: str):
    """
    Allows only digits, spaces, and basic operators.
    Supports + - * / ( ) and decimal points.
    """
    expr = expr.strip()

    # Remove optional "calc " prefix if passed in
    if expr.lower().startswith("calc "):
        expr = expr[5:].strip()

    if not expr:
        print("Usage: calc <expression> (e.g., calc (10+5)*2 )")
        return

    # Validate allowed characters
    if not re.fullmatch(r"[0-9\.\+\-\*\/\(\)\s]+", expr):
        print("❌ Invalid characters. Only numbers and + - * / ( ) are allowed.")
        return

    try:
        result = eval(expr, {"__builtins__": None}, {})
        print("🧮 Result:", result)
    except ZeroDivisionError:
        print("❌ Error: Division by zero.")
    except Exception:
        print("❌ Error: Invalid expression.")

def assistant_bot():
    print("=== Mini Personal Assistant Bot ===")
    print("Commands:")
    print("  time                 -> show current time")
    print("  open <site|url>       -> open website (e.g., open google, open wikipedia, open example.com)")
    print("  calc <expression>     -> calculate (e.g., calc 12/3 + 5)")
    print("  help                 -> show commands")
    print("  exit                 -> quit\n")

    while True:
        cmd = input("You: ").strip()

        if not cmd:
            continue

        low = cmd.lower()

        if low == "exit":
            print("✅ Exiting assistant. Goodbye!")
            break

        elif low == "help":
            print("Commands: time | open <site|url> | calc <expression> | exit")

        elif low == "time":
            show_time()

        elif low.startswith("open"):
            open_website(cmd)

        elif low.startswith("calc"):
            safe_calculate(cmd)

        else:
            print("🤖 I didn't understand. Type 'help' to see commands.")

if __name__ == "__main__":
    assistant_bot()