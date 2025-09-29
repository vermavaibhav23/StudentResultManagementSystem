import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

def register_user():
    name = name_var.get()
    email = email_var.get()
    contact = contact_var.get()
    password = password_var.get()
    question = securityQ_var.get()
    answer = securityA_var.get()

    if not all([name, email, contact, password, question, answer]):
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = sqlite3.connect('srp.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, contact, password, securityQ, securityA) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, email, contact, password, question, answer))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Registration successful!")
        root.destroy()
        subprocess.Popen(["python", "home.py"])

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists!")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def go_home():
    root.destroy()
    subprocess.Popen(["python", "home.py"])

root = tk.Tk()
root.title("Register")
root.state("zoomed")

bg = "#f5f5f5"
root.configure(bg=bg)

frame = tk.Frame(root, bg=bg)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(frame, text="Register", font=("Helvetica", 24, "bold"), bg=bg).grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(frame, text="Name:", bg=bg, font=("Helvetica", 14)).grid(row=1, column=0, sticky="e", padx=10, pady=5)
name_var = tk.StringVar()
tk.Entry(frame, textvariable=name_var, font=("Helvetica", 14), width=30).grid(row=1, column=1)

tk.Label(frame, text="Email:", bg=bg, font=("Helvetica", 14)).grid(row=2, column=0, sticky="e", padx=10, pady=5)
email_var = tk.StringVar()
tk.Entry(frame, textvariable=email_var, font=("Helvetica", 14), width=30).grid(row=2, column=1)

tk.Label(frame, text="Contact:", bg=bg, font=("Helvetica", 14)).grid(row=3, column=0, sticky="e", padx=10, pady=5)
contact_var = tk.StringVar()
tk.Entry(frame, textvariable=contact_var, font=("Helvetica", 14), width=30).grid(row=3, column=1)

tk.Label(frame, text="Password:", bg=bg, font=("Helvetica", 14)).grid(row=4, column=0, sticky="e", padx=10, pady=5)
password_var = tk.StringVar()
tk.Entry(frame, textvariable=password_var, font=("Helvetica", 14), show="*", width=30).grid(row=4, column=1)

tk.Label(frame, text="Security Question:", bg=bg, font=("Helvetica", 14)).grid(row=5, column=0, sticky="e", padx=10, pady=5)
securityQ_var = tk.StringVar()
tk.Entry(frame, textvariable=securityQ_var, font=("Helvetica", 14), width=30).grid(row=5, column=1)

tk.Label(frame, text="Answer:", bg=bg, font=("Helvetica", 14)).grid(row=6, column=0, sticky="e", padx=10, pady=5)
securityA_var = tk.StringVar()
tk.Entry(frame, textvariable=securityA_var, font=("Helvetica", 14), width=30).grid(row=6, column=1)

tk.Button(frame, text="Register", command=register_user, bg="green", fg="white", font=("Helvetica", 12), width=20).grid(row=7, column=0, columnspan=2, pady=15)

tk.Button(frame, text="Back to Home", command=go_home, bg="white", fg="blue", font=("Helvetica", 12, "underline"), bd=0).grid(row=8, column=0, columnspan=2)

root.mainloop()
