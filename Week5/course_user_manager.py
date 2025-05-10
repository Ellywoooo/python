from database import create_connection
import sqlite3

def add_course_user(course, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (course, unit) VALUES (?, ?)", (course, unit))
        conn.commit()
        print(" Course added successfully.")
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

#def delete_user():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS courses")
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")