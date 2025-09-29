import tkinter as tk
from tkinter import ttk
import subprocess

def open_register():
    root.destroy()
    subprocess.Popen(["python", "register.py"])

def open_login():
    root.destroy()
    subprocess.Popen(["python", "login.py"])

# Create the homepage window
root = tk.Tk()
root.title("Student Result Portal")
root.geometry("500x300")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Welcome to Student Result Portal", font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#333")
title.pack(pady=40)

# Buttons
btn_style = {"font": ("Helvetica", 12), "width": 15, "bg": "#4CAF50", "fg": "white", "bd": 0}

btn_register = tk.Button(root, text="Register", command=open_register, **btn_style)
btn_register.pack(pady=10)

btn_login = tk.Button(root, text="Login", command=open_login, **btn_style)
btn_login.pack(pady=10)

root.mainloop()
