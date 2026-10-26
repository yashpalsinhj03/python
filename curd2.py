# curd with menu 
import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    port = 3307,
    user = "root",
    password = ""
)

cursor = con.cursor()
print("mysql connected..")

cursor.execute(
    "CREATE DATABASE IF NOT EXISTS studb"
)
print("database created")
cursor.execute("USE studb")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    mobile VARCHAR(50)
)
""")

print("table created ")

def insert_student():
    firstname = input("enter first name: ")
    lastname = input("enter last name: ")
    mobile = input("enter mobile: ")

    query = """
    INSERT INTO students
    (firstname, lastname, mobile)
    VALUES (%s, %s, %s)
    """
    values = (
      firstname,
      lastname,
      mobile  
    )

    cursor.execute(query, values)
    con.commit()

    print("student inserted...")
    print("student ID:", cursor.lastrowid)

def display_student():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("no student records found.")

    else:
        for row in rows:
            print(
                "ID:", row[0],
                "| first name:", row[1],
                "| last name:", row[2],
                "| mobile:", row[3]
            )
def update_student():
    student_id = input("enter student ID: ")
    firstname = input("enter new first name: ")
    lastname = input("enter new last name: ")
    mobile = input("enter new mobile: ")

    query = """
    UPDATE students
    SET firstname = %s,
        lastname = %s,
        mobile = %s
    WHERE id = %s
    """
    values = (
        firstname,
        lastname,
        mobile,
        student_id
    )

    cursor.execute(query, values)
    con.commit()

    if cursor.rowcount > 0:
        print("student updated..")

    else:
        print("student ID not found.")

def delete_student():
    student_id = input("enter student ID: ")

    query = """
    DELETE FROM students
    WHERE id =%s
    """

    values = (student_id,)
    cursor.execute(query, values)
    con.commit()

    if cursor.rowcount > 0:
        print("student deleted..")

    else:
        print("student ID not found.")

while True:
    print("1. Insert student")
    print("2. Display all student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        insert_student()

    elif choice == "2":
        display_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Progam closed.")

        break

    else:
        print("Invalid choice! please try agin.")

cursor.close()
con.close()

    
