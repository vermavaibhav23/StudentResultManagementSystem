from tkinter import*            #tkinter library provides tools for creating Graphical User Interfaces (GUIs) in Python
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Portal")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg = "white")
        self.root.focus_force()

        #======title=======
        title=Label(self.root, text="Manage Course",font = ("goudy old style",20,"bold"),bg = "#7093A5",fg="white").place(x=10,y=15,width=1180,height=35)

        #=======Variables=====
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        #======widges======
        lbl_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

        #======entry fields of widges======
        self.txt_courseName = Entry(self.root,textvariable=self.var_course, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_courseName.place(x=150, y=60,width=200)
        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg= "lightyellow").place(x=150, y=100,width = 200)
        txt_charges = Entry(self.root,textvariable=self.var_charges, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140,width = 200)
        self.txt_description = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_description.place(x=10, y=180, width = 500, height=100 )

        # =====Buttons=========
        self.btn_add = Button(self.root, text='Save', font=("goudy old style", 15, "bold"), bg="#BDFCC9", fg="#4A9F4F", cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text='Update', font=("goudy old style", 15, "bold"), bg="#CFCFFF", fg="#7093A5", cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="#F8C8DC", fg="#C090AA", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="#F5F5DC", fg="#C1B68F", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        #====Search Panel==========
        self.var_search = StringVar() 

        lbl_search_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white")
        lbl_search_courseName.place(x=720, y=60)

        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_search_courseName.place(x=870, y=60, width=180)

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1070, y=60, width=120, height=28)

        # ========== Content Frame =============
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")

        self.CourseTable["show"] = "headings"

        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=150)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.show()

        # Bind the Treeview to the get_data method
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

    # =======================================================================interact with the database==============================================================

    def clear(self):
        self.show()
    
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0', END)
        self.txt_courseName.config(state=NORMAL)



    def add(self):          #when we click "save" (to add a course).
        con=sqlite3.connect(database="srp.db")      #Connects to database file srp.db.
        cur = con.cursor()                          #Creates a cursor, which is used to execute SQL commands.
                                                    #A cursor in SQLite3 is like a messenger between your Python program and the database. 
                                                    #cursor is used to execute SQL commands and fetch results from the database.
        try:
            if self.var_course.get() == "":                                                      #Checking if Course Name is Empty.
                messagebox.showerror("Error", "Course Name can't be Empty", parent=self.root)    #If course name is empty, shows an error message and stops execution.
            else:                                   #Checks if the course name already exists in the database.
                cur.execute("select * from course where name=?", (self.var_course.get(),))       #This SQL command searches for the course name in the course table.
                row = cur.fetchone()                
                if row != None :                    # (row != None), it means the course already exists.
                    messagebox.showerror("Error","Course Name already Exists", parent=self.root) #thus, error message appears, and the function stops.
                else:                               # If the course does not exist, it gets inserted into the database.
                    cur.execute("insert into course (name, duration, charges, description) values (?, ?, ?, ?)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)
                    ))
                    con.commit()                                                                   #saves the changes permanently to the database.
                    messagebox.showinfo("Success","Course Added Successfully",parent = self.root)  #A message appears saying the course was added successfully.
                    self.show()                                                                    #self.show() is called to refresh the table and display the new course.

        except Exception as ex:                     # If anything goes wrong (e.g., database error, invalid input), an error message is displayed.
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    def update(self):          #when we click "update" (to update a course).
        con=sqlite3.connect(database="srp.db")      #Connects to database file srp.db.
        cur = con.cursor()                          #Creates a cursor, which is used to execute SQL commands.
                                                    #A cursor in SQLite3 is like a messenger between your Python program and the database. 
                                                    #cursor is used to execute SQL commands and fetch results from the database.
        try:
            if self.var_course.get() == "":                                                      #Checking if Course Name is Empty.
                messagebox.showerror("Error", "Course Name can't be Empty", parent=self.root)    #If course name is empty, shows an error message and stops execution.
            else:                                   #Checks if the course name already exists in the database.
                cur.execute("select * from course where name=?", (self.var_course.get(),))       #This SQL command searches for the course name in the course table.
                row = cur.fetchone()                
                if row == None :                   
                    messagebox.showerror("Error","Select Course From List", parent=self.root) 
                else:                               
                    cur.execute("update course set duration=?, charges=?, description=? where name = ?", (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_course.get()
                    ))
                    con.commit()                                                                   
                    messagebox.showinfo("Success","Course Updated Successfully",parent = self.root)  
                    self.show()                                                                    #self.show() is called to refresh the table and display the new course.

        except Exception as ex:                     # If anything goes wrong (e.g., database error, invalid input), an error message is displayed.
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def delete(self):
        con=sqlite3.connect(database="srp.db")      #Connects to database file srp.db.
        cur = con.cursor()                          #Creates a cursor, which is used to execute SQL commands.
                                                    #A cursor in SQLite3 is like a messenger between your Python program and the database. 
                                                    #cursor is used to execute SQL commands and fetch results from the database.
        try:
            if self.var_course.get() == "":                                                      #Checking if Course Name is Empty.
                messagebox.showerror("Error", "Course Name can't be Empty", parent=self.root)    #If course name is empty, shows an error message and stops execution.
            else:                                   
                cur.execute("select * from course where name=?", (self.var_course.get(),))       
                row = cur.fetchone()                
                if row == None :                   
                    messagebox.showerror("Error","Select course from the list first", parent=self.root) #thus, error message appears, and the function stops.
                else:
                    op = messagebox.askyesno("Confirm", "Do you really wanna delete this?", parent=self.root)
                    if op == True:
                        cur.execute("delete from course where name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:                     # If anything goes wrong (e.g., database error, invalid input), an error message is displayed.
            messagebox.showerror("Error", f"Error due to {str(ex)}")




    def search(self):
        con = sqlite3.connect(database="srp.db")
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM course WHERE name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', 'end', values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    #============================================================================Displayin course details in search table=======================================
    def show(self):                                                  #responsible for fetching all course records from the database
                                                                     #and displaying them in a table 
        con=sqlite3.connect(database="srp.db")                       #Connects to the SQLite database named srp.db.
        cur = con.cursor()                                           #Creates a cursor (cur) to execute SQL queries.
        try:
            cur.execute("select * from course")                      #("SELECT * FROM course") → This retrieves all courses from the course table.
            rows = cur.fetchall()                                    #stores all the retrieved records in rows (a list of tuples).
                                                                     #Each row in rows contains (Course ID, Name, Duration, Charges, Description).
            self.CourseTable.delete(*self.CourseTable.get_children()) #Clearing the Table Before Updating
            for row in rows:                                         # Loops through all retrieved rows from the database.
                self.CourseTable.insert('',END,values=row)           #Inserts each row into self.CourseTable (the GUI table) for display.

        except Exception as ex:                                     #If any error occurs, an error message appears instead of crashing the program.
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # ========================== Get Data from Selected Row ==========================
    def get_data(self, ev):
        self.txt_courseName.config(state = 'readonly')
        self.txt_courseName
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]

        if row:  # Ensure row is not empty
            self.var_course.set(row[1])  # Course Name
            self.var_duration.set(row[2])  # Duration
            self.var_charges.set(row[3])  # Charges
            self.txt_description.delete("1.0", END)
            self.txt_description.insert(END, row[4])  # Description

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()