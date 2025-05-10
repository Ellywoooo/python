import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            course_id INTEGER NOT NULL,
            FOREIGN KEY (course_id) REFERENCES courses (id)
        )    
    ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course TEXT NOT NULL,
            unit INTEGER NOT NULL         
        )  
    ''')



    conn.commit()
    conn.close()
