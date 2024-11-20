import time
import pyperclip
from plyer import notification
from detect_sensitive import is_sensitive_data
from log_activity import log_to_html, clear_clipboard


def send_alert(content):
    notification.notify(
        title="Sensitive Data Detected!",
        message=f"Sensitive content detected: {content}",
        timeout=10  
    )



def monitor_clipboard():
    previous_data = ""

    while True:
        try:
            current_data = pyperclip.paste()
            if current_data != previous_data:
                print(f"Clipboard updated: {current_data}")
                
                if is_sensitive_data(current_data):
                    print("Sensitive data detected! Clearing clipboard...")
                    send_alert(current_data)  
                    clear_clipboard()  
                    log_to_html(current_data)  
                previous_data = current_data
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)
