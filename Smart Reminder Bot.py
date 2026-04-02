import time
import sys

def play_sound():
    """Plays a short sound. Works best on Windows; falls back to terminal bell elsewhere."""
    try:
        import winsound  # Windows only
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        # Or use a tone:
        # winsound.Beep(1000, 400)  # frequency (Hz), duration (ms)
    except Exception:
        # Fallback: terminal bell (may or may not beep depending on terminal settings)
        sys.stdout.write("\a")
        sys.stdout.flush()

def smart_reminder_bot():
    print("=== Smart Reminder Bot ===")
    print("Enter seconds (e.g., 10) or type 'exit' to quit.\n")

    while True:
        secs_input = input("Set reminder in seconds: ").strip().lower()
        if secs_input == "exit":
            print("Goodbye!")
            break

        # Validate seconds
        try:
            seconds = float(secs_input)
            if seconds <= 0:
                print("Please enter a number greater than 0.\n")
                continue
        except ValueError:
            print("Invalid input. Enter a number (e.g., 15) or 'exit'.\n")
            continue

        message = input("Reminder message: ").strip()
        if not message:
            message = "Time's up!"

        print(f"\n⏳ Reminder set for {seconds} seconds...")
        time.sleep(seconds)

        print("\n🔔 REMINDER:", message)
        play_sound()
        print()

if __name__ == "__main__":
    smart_reminder_bot()