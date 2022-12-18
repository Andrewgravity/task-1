import mysql.connector
import json

# read data from json
with open('/python/students.json', 'r') as read_file:
    students_data = json.load(read_file)

with open('/python/rooms.json', 'r') as read_file:
    rooms_data = json.load(read_file)

# establish connection to SQL server
connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port = "3306", database = 'db')

print('Database connected')

# INSERT VALUES INTO rooms TABLE
cursor = connection.cursor()
for item in rooms_data:
    id = item.get("id")
    name = item.get("name")
    cursor.execute('INSERT INTO rooms(ROOM_ID, ROOM_NAME) VALUES(%s, %s)', (id, name))

# Create table students
cursor.execute('''
    DROP TABLE IF EXISTS students;
    ''')
cursor.execute('''
    CREATE TABLE students(
    BIRTHDAY DATE NOT NULL,
    STUDENT_ID INT NOT NULL PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL,
    ROOM INT NOT NULL,
    SEX VARCHAR(5) NOT NULL)
    ''')

# INSERT VALUES INTO students TABLE
for item in students_data:
    birthday = item.get("birthday")
    id = item.get("id")
    name = item.get("name")
    room = item.get("room")
    sex = item.get("sex")
    cursor.execute('INSERT INTO students(BIRTHDAY, STUDENT_ID, NAME, ROOM, SEX) VALUES(%s,%s,%s,%s,%s)', (birthday, id, name, room, sex))

print('all data successfully uploaded')

from first_query import query_1
query_1()
# cursor.execute('SELECT * FROM students LIMIT 1')
# students = cursor.fetchone()
# cursor.execute('SELECT * FROM rooms LIMIT 1')
# rooms = cursor.fetchone()
# cursor.execute('SELECT COUNT(1), students.ROOM FROM students INNER JOIN rooms ON students.ROOM = rooms.ROOM_ID GROUP BY students.ROOM')
# test = cursor.fetchall()
# connection.close()

# print(students, '\n', rooms)

# print(test)
