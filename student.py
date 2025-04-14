from tkinter import*            #tkinter library provides tools for creating Graphical User Interfaces (GUIs) in Python
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class studentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Portal")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg = "white")
        self.root.focus_force()

        #======title=======
        title=Label(self.root, text="Manage Student Details",font = ("goudy old style",20,"bold"),bg = "#7093A5",fg="white").place(x=10,y=15,width=1180,height=35)

        #=======Variables=====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_charges=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        self.var_duration=StringVar()

        #======Widgets======
        lbl_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_Email = Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

        lbl_state = Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=220)
        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_state.place(x=150, y=220, width=150)

        lbl_city = Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=310, y=220)
        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_city.place(x=380, y=220, width=100)

        lbl_pin = Label(self.root, text="Pin", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=220)
        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_pin.place(x=570, y=220, width=120)

        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=260)


        #======entry fields of widges======
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_name.place(x=150, y=100, width=200)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_email.place(x=150, y=140, width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values = ("SELECT","Cis Male","Cis Female","Non-Binary","Trans Male","Trans Female","Intersex","Genderfluid","Genderqueer","Agender","Prefer Not to Say","Others"), font=("goudy old style", 15, "bold"), state = 'readonly',justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)


        #============================coulum2 - label n entryfield================================
        

        lbl_dob = Label(self.root, text="DOB", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=100)
        lbl_admission = Label(self.root, text="Admission", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=180)

        self.course_list=[]
        #function call to update list
        self.fetch_course()
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_dob.place(x=480, y=60, width=200)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_contact.place(x=480, y=100, width=200)

        txt_admission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_admission.place(x=480, y=140, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values =self.course_list, font=("goudy old style", 15, "bold"), state = 'readonly',justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Select")

        #======================================================================================================


        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=260, width=540, height=100)


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

        lbl_search_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white")
        lbl_search_roll.place(x=720, y=60)

        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_search_courseName.place(x=870, y=60, width=180)

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1070, y=60, width=120, height=28)

        # ========== Content Frame =============
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob", "contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll", text="Roll No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="PIN")
        self.CourseTable.heading("address", text="Address")

        self.CourseTable["show"] = 'headings'

        self.CourseTable.column("roll", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("admission", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("state", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=100)
        self.CourseTable.column("address", width=200)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

        # Bind the Treeview to the get_data method
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

    # =======================================================================interact with the database==============================================================

    def clear(self):
        self.show()  # Refresh the table
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0", END)  # Clear the address field
        self.txt_roll.config(state=NORMAL)   # Enable the Roll No. field for editing
        self.var_search.set("")              # Clear the search field


    def add(self):          #when we click "save" (to add a course).
        con=sqlite3.connect(database="srp.db")      #Connects to database file srp.db.
        cur = con.cursor()                          #Creates a cursor, which is used to execute SQL commands.
                                                    #A cursor in SQLite3 is like a messenger between your Python program and the database. 
                                                    #cursor is used to execute SQL commands and fetch results from the database.
        try:
            if self.var_roll.get() == "":                                                      #Checking if Course Name is Empty.
                messagebox.showerror("Error", "Roll No. can't be Empty", parent=self.root)    #If course name is empty, shows an error message and stops execution.
            else:                                   #Checks if the course name already exists in the database.
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))       #This SQL command searches for the course name in the course table.
                row = cur.fetchone()                
                if row != None :                    # (row != None), it means the course already exists.
                    messagebox.showerror("Error","Roll Number already Exists", parent=self.root) #thus, error message appears, and the function stops.
                else:                               # If the course does not exist, it gets inserted into the database.
                    cur.execute("insert into student ( roll ,  name ,  email ,  gender ,  dob ,  contact , admission , course , state , city , pin , address ) values (?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()                                                                   #saves the changes permanently to the database.
                    messagebox.showinfo("Success","Student Added Successfully",parent = self.root)  #A message appears saying the course was added successfully.
                    self.show()                                                                    #self.show() is called to refresh the table and display the new course.

        except Exception as ex:                     # If anything goes wrong (e.g., database error, invalid input), an error message is displayed.
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    def update(self):          #when we click "update" (to update a course).
        con=sqlite3.connect(database="srp.db")      #Connects to database file srp.db.
        cur = con.cursor()                          #Creates a cursor, which is used to execute SQL commands.
                                                    #A cursor in SQLite3 is like a messenger between your Python program and the database. 
                                                    #cursor is used to execute SQL commands and fetch results from the database.
        try:
            if self.var_roll.get() == "":                                                      #Checking if Course Name is Empty.
                messagebox.showerror("Error", "Roll No. can't be Empty", parent=self.root)    #If course name is empty, shows an error message and stops execution.
            else:                                   #Checks if the course name already exists in the database.
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))       #This SQL command searches for the course name in the course table.
                row = cur.fetchone()                
                if row == None :                   
                    messagebox.showerror("Error","Select student From List", parent=self.root) 
                else:                               
                    cur.execute("update student set name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? where roll=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get()
                    ))

                    con.commit()                                                                   
                    messagebox.showinfo("Success","Course Updated Successfully",parent = self.root)  
                    self.show()                                                                    #self.show() is called to refresh the table and display the new course.

        except Exception as ex:                     # If anything goes wrong (e.g., database error, invalid input), an error message is displayed.
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def delete(self):
        con = sqlite3.connect(database="srp.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":  # Check if Roll No. is empty
                messagebox.showerror("Error", "Roll No. can't be Empty", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:  # If no student is found with the given Roll No.
                    messagebox.showerror("Error", "Select student from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete this student?", parent=self.root)
                    if op:  # If user confirms deletion
                        cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student deleted successfully", parent=self.root)
                        self.clear()  # Clear the form after deletion
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def search(self):
        con = sqlite3.connect(database="srp.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE roll=?" , (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    #============================================================================Displayin course details in search table=======================================
    def show(self):                                                  #responsible for fetching all course records from the database
                                                                     #and displaying them in a table 
        con=sqlite3.connect(database="srp.db")                       #Connects to the SQLite database named srp.db.
        cur = con.cursor()                                           #Creates a cursor (cur) to execute SQL queries.
        try:
            cur.execute("select * from student")                      #("SELECT * FROM course") → This retrieves all courses from the course table.
            rows = cur.fetchall()                                    #stores all the retrieved records in rows (a list of tuples).
                                                                     #Each row in rows contains (Course ID, Name, Duration, Charges, Description).
            self.CourseTable.delete(*self.CourseTable.get_children()) #Clearing the Table Before Updating
            for row in rows:                                         # Loops through all retrieved rows from the database.
                self.CourseTable.insert('',END,values=row)           #Inserts each row into self.CourseTable (the GUI table) for display.

        except Exception as ex:                                     #If any error occurs, an error message appears instead of crashing the program.
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    
    def fetch_course(self):
        con = sqlite3.connect(database="srp.db")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])

            #print(v)
            #self.course_list=v

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # ========================== Get Data from Selected Row ==========================
    def get_data(self, ev):
        self.txt_roll.config(state = 'readonly')
        
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]

        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])

if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()