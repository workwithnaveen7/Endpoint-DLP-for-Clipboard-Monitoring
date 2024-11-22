import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

USERNAME = "admin"
PASSWORD = "password"

def verify_login(username, password):
    return username == USERNAME and password == PASSWORD

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if verify_login(username, password):
        root.destroy()  # Close the login window
        # Run the main.py script
        subprocess.Popen([sys.executable, 'main.py'])  # Use sys.executable to run the script with the same Python interpreter
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# Create the login window
root = tk.Tk()
root.title("Login")

label_username = tk.Label(root, text="Username")
label_username.pack(padx=10, pady=5)

entry_username = tk.Entry(root)
entry_username.pack(padx=10, pady=5)

label_password = tk.Label(root, text="Password")
label_password.pack(padx=10, pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(padx=10, pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

root.mainloop()
