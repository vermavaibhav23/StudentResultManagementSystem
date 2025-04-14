import sqlite3

# SQLite3 is a simple database that stores data in a single file on your computer. 
# It does not need a server, making it easy to use and super fast for small projects.

def create_db():
    """Function to create the database and tables if they do not exist."""

    # Connect to (or create) the database file 'srp.db'
    con = sqlite3.connect(database="srp.db")

    # Create a cursor to execute SQL commands
    cur = con.cursor()

    # Create 'course' table if it does not exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration TEXT,
            charges TEXT,
            description TEXT
        )
    """)
    
    # Commit changes to the database
    con.commit()

    # Create 'Student' table if it does not exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            roll INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            admission TEXT,
            course TEXT,
            state TEXT,
            city TEXT,
            pin TEXT,
            address TEXT
        )
    """)

    # Commit changes to the database
    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS result (
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            course TEXT,
            marks_ob TEXT,
            full_marks TEXT,
            per TEXT
        )
    """)
    
    # Commit changes to the database
    con.commit()

    # Close the database connection
    con.close()

# Call the function to create the database and tables
create_db()
