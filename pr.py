import sqlite3

DB = "students.db"

def connect():
    return sqlite3.connect(DB)

def setup():
    conn = connect()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        grade INTEGER,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_student():
    name = input("Name: ")
    grade = input("Grade: ")
    email = input("Email: ")
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO students(name, grade, email) VALUES(?,?,?)",
              (name, grade, email))
    conn.commit()
    conn.close()
    print("Added.")

def view_students():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    if not rows:
        print("No data.")
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")
    conn.close()

def search_student():
    s = input("Search: ")
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE name LIKE ? OR email LIKE ?",
              (f"%{s}%", f"%{s}%"))
    rows = c.fetchall()
    if not rows:
        print("No match.")
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")
    conn.close()

def update_student():
    view_students()
    sid = input("ID to update: ")
    conn = connect()
    c = conn.cursor()
    name = input("New name: ")
    grade = input("New grade: ")
    email = input("New email: ")
    if name:
        c.execute("UPDATE students SET name=? WHERE id=?", (name, sid))
    if grade:
        c.execute("UPDATE students SET grade=? WHERE id=?", (grade, sid))
    if email:
        c.execute("UPDATE students SET email=? WHERE id=?", (email, sid))
    conn.commit()
    conn.close()
    print("Updated.")

def delete_student():
    view_students()
    sid = input("ID to delete: ")
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    conn.close()
    print("Deleted.")

def menu():
    while True:
        print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
        ch = input("Choice: ")
        if ch == "1": add_student()
        elif ch == "2": view_students()
        elif ch == "3": search_student()
        elif ch == "4": update_student()
        elif ch == "5": delete_student()
        elif ch == "6": break

setup()
menu()
