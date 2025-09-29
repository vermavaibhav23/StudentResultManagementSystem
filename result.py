from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class resultClass:
    def __init__(self, root, user_id):
        self.root = root
        self.user_id = user_id
        self.root.title("Student Result Portal")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # ====== Variables ======
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []

        self.fetch_roll()

        # ====== Title ======
        Label(self.root, text="Add Student Result", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)

        # ====== Labels and Entries ======
        Label(self.root, text="Select Student", font=("goudy old style", 20, "bold")).place(x=50, y=100)
        Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=160)
        Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=220)
        Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=280)
        Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list,
                                        font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
               cursor="hand2", command=self.search).place(x=500, y=100, width=100, height=28)

        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=160, width=320)
        Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=220, width=320)
        Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=280, width=320)
        Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=340, width=320)

        Button(self.root, text="Submit", font=("times new roman", 15), bg="lightgreen", activebackground="lightgreen", cursor="hand2",
               command=self.add).place(x=300, y=420, width=120, height=35)

        Button(self.root, text="Clear", font=("times new roman", 15), bg="lightgray", activebackground="lightgray", cursor="hand2",
               command=self.clear).place(x=430, y=420, width=120, height=35)

        # ====== Background Image ======
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((500, 300))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        Label(self.root, image=self.bg_img).place(x=630, y=100)

    # ====== Fetch Roll Numbers Based on user_id ======
    def fetch_roll(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student WHERE user_id=?", (self.user_id,))
            rows = cur.fetchall()
            self.roll_list = [row[0] for row in rows]
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # ====== Search student details ======
    def search(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, course FROM student WHERE roll=? AND user_id=?", (self.var_roll.get(), self.user_id))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # ====== Add Result ======
    def add(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Please search student's record first", parent=self.root)
            elif self.var_marks.get() == "" or self.var_full_marks.get() == "":
                messagebox.showerror("Error", "Please enter marks and full marks", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=? AND course=? AND user_id=?", (self.var_roll.get(), self.var_course.get(), self.user_id))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Result already exists", parent=self.root)
                else:
                    per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                    cur.execute("""INSERT INTO result (roll, name, course, marks_ob, full_marks, per, user_id)
                                   VALUES (?, ?, ?, ?, ?, ?, ?)""", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per),
                        self.user_id
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)

                    self.roll_list.clear()
                    self.fetch_roll()
                    self.txt_student["values"] = self.roll_list
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")
        self.txt_student.set("Select")

if __name__ == "__main__":
    root = Tk()
    resultClass(root, user_id=1)  # for testing
    root.mainloop()
