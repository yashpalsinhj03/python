#  normal curd 
import mysql.connector

con = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = ""
)

cursor = con.cursor()

print("mysql connected successfully")

cursor.execute(
      "CREATE  DATABASE IF NOT EXISTS coleagedb"
)
print("database created successfully")


cursor.execute(
      "USE coleagedb"
)


cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
      id INT AUTO_INCREMENT PRIMARY KEY,
      firstname VARCHAR(100),
      lastname VARCHAR(100),
      mobile VARCHAR(15),
      email VARCHAR(100)
)
""")

print("table created")
cursor.execute("TRUNCATE TABLE students")
con.commit()

insert_query = """
INSERT INTO students
(firstname, lastname, mobile, email)
VALUES (%s, %s, %s, %s)
"""
insert_values = (
      "ivar",
      "lothbrock",
      "1234567890",
      "ivar@gamil.com"
)

cursor.execute(insert_query, insert_values)

insert_values = (
    "ragnar",
    "lothbrock",
    "9876543210",
    "ragnar@gmail.com"
)

cursor.execute(insert_query, insert_values)

cursor.execute(
      "SELECT * FROM students"
)

rows = cursor.fetchall()

print("\n----student data----")

for row in rows:
      print(row)

update_query = """ UPDATE students SET mobile = %s WHERE id = %s"""
update_values = ("7878789966",1)
cursor.execute(update_query, update_values)
con.commit()

print("\n----data updatedd")

cursor.execute(
      "SELECT * FROM students"

)

rows = cursor.fetchall()

print("\n-----updated student data")
for row in rows:
      print(row)

delete_query = """DELETE FROM students WHERE ID = %s """
delete_values = (1,)

cursor.execute(
      delete_query,
      delete_values
)
con.commit()
print("\n---deletedd data----")

cursor.execute(
      "SELECT * FROM students"
)

rows = cursor.fetchall()
print("\n---final data----")
for row in rows:
      print(row)

cursor.close()
con.close()
print("\nmysql connection closed")