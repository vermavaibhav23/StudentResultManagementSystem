from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
import sqlite3
import sys

class SRP:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Student Result Portal")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.user_id = user_id

        # ========== icons ==========
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # ========== title ==========
        title = Label(self.root, text="Student Result Portal", padx=10, compound=LEFT, image=self.logo_dash,
                      font=("goudy old style", 20, "bold"), bg="#0b5377", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # ========== menu ==========
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)

        Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_student).place(x=240, y=5, width=200, height=40)

        Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)

        Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.add_report).place(x=680, y=5, width=200, height=40)

        Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.logout).place(x=900, y=5, width=200, height=40)

        Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
               cursor="hand2", command=self.root.quit).place(x=1120, y=5, width=200, height=40)

        # ========== content window ==========
        self.bg_img = Image.open("images/bg.png").resize((920, 350))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)

        # ========== summary blocks ==========
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="#AEC6CF")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                 relief=RIDGE, bg="#FFB347")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="#C3B1E1")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # ========== footer ==========
        footer = Label(self.root,
                       text="Student Result Portal\nContact Us for any Technical Issues - @Vaibhav & @Samriddhi",
                       font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        self.update_counts()

    def update_counts(self):
        con = sqlite3.connect("srp.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM course WHERE user_id=?", (self.user_id,))
            course_count = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM student WHERE user_id=?", (self.user_id,))
            student_count = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM result WHERE user_id=?", (self.user_id,))
            result_count = cur.fetchone()[0]

            self.lbl_course.config(text=f"Total Courses\n[ {course_count} ]")
            self.lbl_student.config(text=f"Total Students\n[ {student_count} ]")
            self.lbl_result.config(text=f"Total Results\n[ {result_count} ]")

        except Exception as e:
            print("Error updating counts:", e)
        finally:
            con.close()

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win, self.user_id)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win, self.user_id)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win, self.user_id)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win, self.user_id)

    def logout(self):
        self.root.destroy()
        import subprocess, sys
        subprocess.Popen([sys.executable, "home.py"])

# ========== ENTRY POINT ==========
if __name__ == "__main__":
    import sys
    user_id = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    root = Tk()
    obj = SRP(root, user_id)
    root.mainloop()
