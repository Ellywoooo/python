from database import create_connection
import sqlite3

def add_user(name, email, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, course_id) VALUES (?, ?, ?)", 
                       (name, email, course_id))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")

# Search the user based on ID and name   
def advanced_user(name, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ? AND name LIKE ?", ( user_id, '%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Search the user based on course_id and user name   
def course_id_name_user(name, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT users.name, users.email, courses.course, courses.unit 
                   FROM users
                   JOIN courses ON users.course_id = courses.id 
                   WHERE courses.id = ? AND users.name LIKE ? 
                   """, ( course_id, '%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

