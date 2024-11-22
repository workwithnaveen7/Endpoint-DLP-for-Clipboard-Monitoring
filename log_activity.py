import mysql.connector
from datetime import datetime

# MySQL database connection setup
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Replace with your MySQL username
        password="2005",        # Replace with your MySQL password
        database="clipboard_monitor"
    )

def log_to_db(data):
    try:
        # Connect to MySQL
        conn = connect_to_db()
        cursor = conn.cursor()

        # Insert sensitive data into logs table
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO logs (content, timestamp) VALUES (%s, %s)", (data, timestamp))

        conn.commit()
        cursor.close()
        conn.close()
        print("Sensitive data logged to MySQL database")
    except Exception as e:
        print(f"Error logging data to MySQL: {e}")

def clear_clipboard():
    try:
        import pyperclip
        pyperclip.copy("")  # Clear the clipboard
        print("Clipboard cleared.")
    except Exception as e:
        print(f"Error clearing clipboard: {e}")
