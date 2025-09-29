import tkinter as tk
from tkinter import messagebox
import sqlite3

def reset_password():
    email = email_var.get()
    question = question_var.get()
    answer = answer_var.get()
    new_pass = new_password_var.get()

    conn = sqlite3.connect('srp.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND securityQ = ? AND securityA = ?", (email, question, answer))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE users SET password = ? WHERE email = ?", (new_pass, email))
        conn.commit()
        messagebox.showinfo("Success", "Password updated successfully!")
        root.destroy()
    else:
        messagebox.showerror("Error", "Invalid details provided.")
    
    conn.close()

root = tk.Tk()
root.title("Forgot Password")
root.state("zoomed")
bg = "#f5f5f5"
root.configure(bg=bg)

frame = tk.Frame(root, bg=bg)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(frame, text="Reset Password", font=("Helvetica", 24, "bold"), bg=bg).grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(frame, text="Email:", font=("Helvetica", 14), bg=bg).grid(row=1, column=0, sticky="e", padx=10, pady=5)
email_var = tk.StringVar()
tk.Entry(frame, textvariable=email_var, font=("Helvetica", 14), width=30).grid(row=1, column=1)

tk.Label(frame, text="Security Question:", font=("Helvetica", 14), bg=bg).grid(row=2, column=0, sticky="e", padx=10, pady=5)
question_var = tk.StringVar()
tk.Entry(frame, textvariable=question_var, font=("Helvetica", 14), width=30).grid(row=2, column=1)

tk.Label(frame, text="Answer:", font=("Helvetica", 14), bg=bg).grid(row=3, column=0, sticky="e", padx=10, pady=5)
answer_var = tk.StringVar()
tk.Entry(frame, textvariable=answer_var, font=("Helvetica", 14), width=30).grid(row=3, column=1)

tk.Label(frame, text="New Password:", font=("Helvetica", 14), bg=bg).grid(row=4, column=0, sticky="e", padx=10, pady=5)
new_password_var = tk.StringVar()
tk.Entry(frame, textvariable=new_password_var, font=("Helvetica", 14), show="*", width=30).grid(row=4, column=1)

tk.Button(frame, text="Reset Password", command=reset_password, bg="green", fg="white", font=("Helvetica", 12), width=20).grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
