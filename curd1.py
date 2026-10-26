import mysql.connector

# step 1 connect to server

con = mysql.connector.connect(
      host = "localhost",
      port = 3307,
      user = "root",
      password = ""
)

cursor = con.cursor()

print("mysql connected successfully")

# step 2 create database

cursor.execute(
      "CREATE  DATABASE IF NOT EXISTS coleagedb"
)
print("database created successfully")

# step 3 
cursor.execute(
      "USE coleagedb"
)

# step 4 create table

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

# sstep 5 insert data

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

# step 6 read data
cursor.execute(
      "SELECT * FROM students"
)

rows = cursor.fetchall()

print("\n----student data----")

for row in rows:
      print(row)


# step 7 update data

update_query = """ UPDATE students SET mobile = %s WHERE id = %s"""
update_values = ("7878789966",1)
cursor.execute(update_query, update_values)
con.commit()

print("\n----data updatedd")

# step 8 read data
cursor.execute(
      "SELECT * FROM students"

)

rows = cursor.fetchall()

print("\n-----updated student data")
for row in rows:
      print(row)

# step 9 delete data
delete_query = """DELETE FROM students WHERE ID = %s """
delete_values = (1,)

cursor.execute(
      delete_query,
      delete_values
)
con.commit()
print("\n---deletedd data----")

# step 10 read data
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