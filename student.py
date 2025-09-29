from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class studentClass:
    def __init__(self, root, user_id):
        self.root = root
        self.user_id = user_id
        self.root.title("Student Result Portal")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Variables ===
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

        # === Title ===
        Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), bg="#7093A5", fg="white").place(x=10, y=15, width=1180, height=35)

        # === Widgets ===
        Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)

        Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100, width=200)

        Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140, width=200)

        Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                       values=("SELECT", "Male", "Female", "Other"), state='readonly',
                                       font=("goudy old style", 15, "bold"), justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=220)
        Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=220, width=150)

        Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=310, y=220)
        Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=380, y=220, width=100)

        Label(self.root, text="Pin", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=220)
        Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=570, y=220, width=120)

        Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=260)
        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=260, width=540, height=100)

        Label(self.root, text="DOB", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=60, width=200)

        Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=100)
        Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=100, width=200)

        Label(self.root, text="Admission", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=140)
        Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=140, width=200)

        Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=180)
        self.course_list = []
        self.fetch_course()
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, state="readonly",
                                       font=("goudy old style", 15, "bold"), justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Select")

        # Buttons
        Button(self.root, text='Save', font=("goudy old style", 15, "bold"), bg="#BDFCC9", fg="#4A9F4F", cursor="hand2", command=self.add).place(x=150, y=400, width=110, height=40)
        Button(self.root, text='Update', font=("goudy old style", 15, "bold"), bg="#CFCFFF", fg="#7093A5", cursor="hand2", command=self.update).place(x=270, y=400, width=110, height=40)
        Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="#F8C8DC", fg="#C090AA", cursor="hand2", command=self.delete).place(x=390, y=400, width=110, height=40)
        Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="#F5F5DC", fg="#C1B68F", cursor="hand2", command=self.clear).place(x=510, y=400, width=110, height=40)

        # Search
        Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        Button(self.root, text="Search", command=self.search, font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white").place(x=1070, y=60, width=120, height=28)

        # Table
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        for col in self.CourseTable["columns"]:
            self.CourseTable.heading(col, text=col.capitalize())
            self.CourseTable.column(col, width=100)

        self.CourseTable["show"] = "headings"
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # ========================= Other methods (add, update, delete, show, search, etc.) remain unchanged =========================
    # You already posted them correctly — they work perfectly with user_id filtering, course dropdown, and clean table logic.

if __name__ == "__main__":
    root = Tk()
    studentClass(root, user_id=1)
    root.mainloop()
