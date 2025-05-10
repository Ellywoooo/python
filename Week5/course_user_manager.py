from database import create_connection
import sqlite3

def add_course_user(name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Error")
    conn.close()

def search_course_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_course_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows
