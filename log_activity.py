import mysql.connector
from datetime import datetime

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",      
        password="2005",       
        database="clipboard_monitor"
    )

def log_to_db(data):
    try:

        conn = connect_to_db()
        cursor = conn.cursor()

 
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
        pyperclip.copy("") 
        print("Clipboard cleared.")
    except Exception as e:
        print(f"Error clearing clipboard: {e}")
