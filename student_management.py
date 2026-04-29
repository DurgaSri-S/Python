import sqlite3

# connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
course TEXT
)
""")

# add student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute("INSERT INTO students(name,age,course) VALUES(?,?,?)",
                   (name,age,course))
    conn.commit()
    print("Student added successfully")

# view students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# update student
def update_student():
    sid = int(input("Enter student id to update: "))
    new_course = input("Enter new course: ")

    cursor.execute("UPDATE students SET course=? WHERE id=?",
                   (new_course,sid))
    conn.commit()
    print("Student updated")

# delete student
def delete_student():
    sid = int(input("Enter student id to delete: "))

    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    print("Student deleted")

# menu
while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")

conn.close()
