from datetime import datetime
import pyperclip

def log_to_html(data):

    file_name = "sensitive_clipboard_logs.html"

    try:
        with open(file_name, "a") as file:

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"""
            <div style="border: 1px solid #ddd; margin: 10px; padding: 10px;">
                <p><strong>Timestamp:</strong> {timestamp}</p>
                <p><strong>Content:</strong> {data}</p>
            </div>
            """
            file.write(entry)

        print(f"Sensitive data logged to {file_name}")
    except Exception as e:
        print(f"Error writing to HTML file: {e}")

def clear_clipboard():
    try:
        pyperclip.copy("")  
        print("Clipboard cleared.")
    except Exception as e:
        print(f"Error clearing clipboard: {e}")
