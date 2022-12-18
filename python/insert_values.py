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
    cursor.execute('INSERT INTO rooms(ID, NAME) VALUES(%s,%s)', (id, name))

# INSERT VALUES INTO students TABLE
for item in students_data:
    birthday = item.get("birthday")
    id = item.get("id")
    name = item.get("name")
    room = item.get("room")
    sex = item.get("sex")
    cursor.execute('INSERT INTO students(BIRTHDAY, ID, NAME, ROOM_ID, SEX) VALUES(%s,%s,%s,%s,%s)', (birthday, id, name, room, sex))

sequence = cursor.column_names
print(sequence)

cursor.execute('SELECT * FROM students LIMIT 1')
students = cursor.fetchone()
cursor.execute('SELECT * FROM rooms LIMIT 1')
rooms = cursor.fetchone()
connection.close()

print(students, '\n', rooms)