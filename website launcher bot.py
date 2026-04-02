import webbrowser

def website_launcher_bot():
    # Add / edit websites here (supports 5+)
    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "wikipedia": "https://www.wikipedia.org",
        "twitter": "https://x.com",
        "linkedin": "https://www.linkedin.com",
    }

    print("=== Website Launcher Bot ===")
    print("Type a site name to open it:", ", ".join(sorted(sites.keys())))
    print("Type 'list' to see commands, or 'exit' to stop.\n")

    while True:
        cmd = input("Command: ").strip().lower()

        if cmd == "exit":
            print("Bot stopped. Goodbye!")
            break

        elif cmd == "list":
            print("Available sites:", ", ".join(sorted(sites.keys())))

        elif cmd in sites:
            url = sites[cmd]
            webbrowser.open(url, new=2)  # new=2 => open in a new tab if possible
            print(f"Opening: {url}")

        else:
            print("Unknown command. Type 'list' to see available sites, or 'exit' to quit.")

if __name__ == "__main__":
    website_launcher_bot()