# course.py
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
    def __init__(self, root, user_id):
        self.root = root
        self.user_id = user_id
        self.root.title("Manage Course")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()

        Label(self.root, text="Manage Course", font=("goudy old style", 20, "bold"),
              bg="#7093A5", fg="white").place(x=10, y=15, width=1180, height=35)

        # Fields
        labels = ["Course Name", "Duration", "Charges", "Description"]
        for i, label in enumerate(labels):
            Label(self.root, text=label, font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60 + i * 40)

        self.txt_courseName = Entry(self.root, textvariable=self.var_course,
                                    font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_courseName.place(x=150, y=60, width=200)
        Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"),
              bg="lightyellow").place(x=150, y=100, width=200)
        Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, "bold"),
              bg="lightyellow").place(x=150, y=140, width=200)

        self.txt_description = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_description.place(x=10, y=180, width=500, height=100)

        # Buttons
        actions = [("Save", self.add), ("Update", self.update), ("Delete", self.delete), ("Clear", self.clear)]
        for i, (text, command) in enumerate(actions):
            Button(self.root, text=text, font=("goudy old style", 15, "bold"), bg="#DDD",
                   cursor="hand2", command=command).place(x=150 + i * 120, y=400, width=110, height=40)

        # Search
        Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"),
              bg="white").place(x=720, y=60)
        Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"),
              bg="lightyellow").place(x=870, y=60, width=180)
        Button(self.root, text="Search", font=("goudy old style", 15, "bold"),
               command=self.search, bg="#03a9f4", fg="white", cursor="hand2").place(x=1070, y=60, width=120, height=28)

        # Table
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        for col in ["cid", "name", "duration", "charges", "description"]:
            self.CourseTable.heading(col, text=col.capitalize())
            self.CourseTable.column(col, width=100)
        self.CourseTable["show"] = "headings"
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def clear(self):
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", END)
        self.txt_courseName.config(state=NORMAL)
        self.show()

    def add(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name can't be Empty", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=? AND user_id=?", (self.var_course.get(), self.user_id))
                if cur.fetchone():
                    messagebox.showerror("Error", "Course already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO course (name, duration, charges, description, user_id) VALUES (?, ?, ?, ?, ?)",
                                (self.var_course.get(), self.var_duration.get(), self.var_charges.get(),
                                 self.txt_description.get("1.0", END).strip(), self.user_id))
                    con.commit()
                    messagebox.showinfo("Success", "Course added", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))
        finally:
            con.close()

    def update(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course WHERE name=? AND user_id=?", (self.var_course.get(), self.user_id))
            if not cur.fetchone():
                messagebox.showerror("Error", "Select course from list", parent=self.root)
            else:
                cur.execute("UPDATE course SET duration=?, charges=?, description=? WHERE name=? AND user_id=?",
                            (self.var_duration.get(), self.var_charges.get(),
                             self.txt_description.get("1.0", END).strip(), self.var_course.get(), self.user_id))
                con.commit()
                messagebox.showinfo("Updated", "Course updated", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course WHERE name=? AND user_id=?", (self.var_course.get(), self.user_id))
            if not cur.fetchone():
                messagebox.showerror("Error", "Select course from list", parent=self.root)
            else:
                if messagebox.askyesno("Confirm", "Really delete?", parent=self.root):
                    cur.execute("DELETE FROM course WHERE name=? AND user_id=?", (self.var_course.get(), self.user_id))
                    con.commit()
                    self.clear()
                    messagebox.showinfo("Deleted", "Course deleted", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", str(ex))
        finally:
            con.close()

    def search(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course WHERE name LIKE ? AND user_id=?", (f'%{self.var_search.get()}%', self.user_id))
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", str(ex))
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course WHERE user_id=?", (self.user_id,))
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", str(ex))
        finally:
            con.close()

    def get_data(self, ev):
        self.txt_courseName.config(state="readonly")
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        if row:
            self.var_course.set(row[1])
            self.var_duration.set(row[2])
            self.var_charges.set(row[3])
            self.txt_description.delete("1.0", END)
            self.txt_description.insert(END, row[4])
