import time

def secure_login():
    correct_password = "Admin123"   # Change this to your password
    max_attempts = 3
    attempts = 0

    print("=== Secure Login System ===")

    while attempts < max_attempts:
        password = input("Enter Password: ")

        if password == correct_password:
            print("\n✅ Access Granted!")
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"❌ Incorrect Password! Attempts remaining: {remaining}\n")

    print("🚫 System Locked! Too many failed attempts.")
    time.sleep(2)

if __name__ == "__main__":
    secure_login()