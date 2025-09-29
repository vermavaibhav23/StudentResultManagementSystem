import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
import sys

def login_user():
    email = email_var.get()
    password = password_var.get()

    if not email or not password:
        messagebox.showerror("Error", "Both fields are required")
        return

    conn = sqlite3.connect('srp.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM users WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        user_id, user_name = result
        messagebox.showinfo("Login", f"Welcome, {user_name}!")

        root.destroy()
        # Pass user_id to dashboard
        subprocess.Popen([sys.executable, "dashboard.py", str(user_id)])
    else:
        messagebox.showerror("Login", "Invalid email or password")

def open_forgot():
    root.destroy()
    subprocess.Popen([sys.executable, "forgot_password.py"])

# ---------- GUI ----------

root = tk.Tk()
root.title("Login")
root.state('zoomed')  # Fullscreen

bg = "#f5f5f5"
root.configure(bg=bg)

frame = tk.Frame(root, bg=bg)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(frame, text="Login", font=("Helvetica", 24, "bold"), bg=bg).grid(row=0, column=0, columnspan=2, pady=20)

# Email
tk.Label(frame, text="Email:", font=("Helvetica", 14), bg=bg).grid(row=1, column=0, sticky="e", padx=10, pady=5)
email_var = tk.StringVar()
tk.Entry(frame, textvariable=email_var, font=("Helvetica", 14), width=30).grid(row=1, column=1, pady=5)

# Password
tk.Label(frame, text="Password:", font=("Helvetica", 14), bg=bg).grid(row=2, column=0, sticky="e", padx=10, pady=5)
password_var = tk.StringVar()
tk.Entry(frame, textvariable=password_var, font=("Helvetica", 14), width=30, show="*").grid(row=2, column=1, pady=5)

# Login Button
tk.Button(frame, text="Login", command=login_user, bg="green", fg="white", font=("Helvetica", 12), width=20).grid(row=3, column=0, columnspan=2, pady=15)

# Forgot Password Link
tk.Button(frame, text="Forgot Password?", command=open_forgot, bg="white", fg="blue",
          font=("Helvetica", 12, "underline"), bd=0).grid(row=4, column=0, columnspan=2)

root.mainloop()
