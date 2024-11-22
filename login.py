import tkinter as tk
from tkinter import messagebox, font
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
        root.destroy()  
        subprocess.Popen([sys.executable, 'main.py'])  
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")


root = tk.Tk()
root.title("Endpoint DLP for Clipboard Monitoring")


window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

root.configure(bg="#f0f0f0")
font_style = font.Font(family="Helvetica", size=12)

header_label = tk.Label(root, text="Login to your account", font=("Helvetica", 16, "bold"), bg="#f0f0f0", pady=10)
header_label.pack()


label_username = tk.Label(root, text="Username", font=font_style, bg="#f0f0f0")
label_username.pack(padx=10, pady=5)
entry_username = tk.Entry(root, font=font_style, bd=2, relief="solid", width=25)
entry_username.pack(padx=10, pady=5)
entry_username.focus() 


label_password = tk.Label(root, text="Password", font=font_style, bg="#f0f0f0")
label_password.pack(padx=10, pady=5)
entry_password = tk.Entry(root, show="*", font=font_style, bd=2, relief="solid", width=25)
entry_password.pack(padx=10, pady=5)


login_button = tk.Button(root, text="Login", font=font_style, bg="#4CAF50", fg="white", bd=0, width=15, command=login)
login_button.pack(pady=20)


footer_label = tk.Label(root, text="© 2024 MyCompany", font=("Helvetica", 10), bg="#f0f0f0")
footer_label.pack(pady=5)



root.mainloop()
