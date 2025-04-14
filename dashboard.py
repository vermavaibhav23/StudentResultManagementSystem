from tkinter import*
#tkinter library provides tools for creating Graphical User Interfaces (GUIs) in Python
from PIL import Image, ImageTk  #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass

class SRP:   #main class
    def __init__(self,root):    
        self.root=root                             #root is the main application window.
        self.root.title("Student Result Portal")   #Sets the title of the window to "Student Result Portal"
        self.root.geometry("1350x700+0+0")         #Defines window size (1350x700) and position (0+0 = top-left of screen).
        self.root.config(bg = "white")             #Sets background color.

        #=====icons=======
        self.logo_dash=ImageTk.PhotoImage(file = "images/logo_p.png")   #Loads an image (logo_p.png) as the application's logo.

        #======title=======                                              Adding the Title Label
        title=Label(self.root, text="Student Result Portal",padx=10,compound=LEFT,image=self.logo_dash,font = ("goudy old style",20,"bold"),bg = "#0b5377",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #======menu=======
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")       #Creates a frame to hold menu buttons.
        M_Frame.place(x=10, y=70, width=1340, height=80)                                              #The frame is placed below the title.

        #Adding Buttons Inside the Menu Frame
        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command = self.add_course ).place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command = self.add_student ).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command = self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command = self.add_report).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2").place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2").place(x=1120, y=5, width=200, height=40)


        # ======content window======Adding a Background Image
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350))  
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)

        # =======updated=======Displaying Total Counts (Courses, Students, Results)
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#AEC6CF")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student= Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#FFB347")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#C3B1E1")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)


        #======footer=======Displays contact information(in case of technical issues) at the bottom.
        footer=Label(self.root, text="Student Result Portal\nContact Us for any Technical Issues - @Vaibhav & @Samriddhi",font = ("goudy old style",12),bg = "#262626",fg="white").pack(side=BOTTOM, fill=X)




    def add_course(self):                 #When the "Course" button is clicked, this function creates a new window (Toplevel).
        self.new_win=Toplevel(self.root)  #CourseClass(self.new_win) loads the Course Management page.
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)




if __name__ == "__main__":
    root = Tk()                         #Creates the main window (root).
    obj = SRP(root)                     #Creates an instance of SRP(root) (which initializes the GUI).
    root.mainloop()                     #Runs the application (mainloop()).