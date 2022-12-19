import mysql.connector
import json
from sql_queries import query_1

# read data from json
with open('/python/students.json', 'r') as read_file:
    students_data = json.load(read_file)

with open('/python/rooms.json', 'r') as read_file:
    rooms_data = json.load(read_file)

# establish connection to SQL server
connection = mysql.connector.connect(
    user='root', password='root', host='db-server', port = "3306", database = 'db')

print('Database connected')

# INSERT VALUES INTO rooms TABLE
cursor = connection.cursor()
for item in rooms_data:
    id = item.get("id")
    name = item.get("name")
    cursor.execute('INSERT INTO Room(Id, Name) VALUES(%s, %s)', (id, name))

# INSERT VALUES INTO students TABLE
for item in students_data:
    birthday = item.get("birthday")
    id = item.get("id")
    name = item.get("name")
    room = item.get("room")
    sex = item.get("sex")
    cursor.execute('INSERT INTO Student(Birthday, Id, Name, RoomId, Sex) VALUES(%s,%s,%s,%s,%s)', (birthday, id, name, room, sex))

print('all data successfully uploaded')


print('starting query 1')
var = query_1()
print('query 1 done')
# # from first_query import query_1
# # query_1()
# cursor.execute('SELECT * FROM Student LIMIT 1')

# columns = cursor.description 
# result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

# print(result)

# cursor.execute('SELECT COUNT(1) AS Number_of_students, Student.RoomId FROM Student INNER JOIN Room ON Student.RoomId = Room.Id GROUP BY Student.RoomId')
# query1 = cursor.fetchall()
# cursor.execute('''
#     SELECT Room.Id, AVG(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) AS age
#     FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
#     GROUP BY Room.Id
#     ORDER BY age ASC
#     LIMIT 5;''')
# query2 = cursor.fetchall()
# cursor.execute('''
#     SELECT Room.Id, MAX(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) - MIN(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) AS age
#     FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
#     GROUP BY Room.Id
#     ORDER BY age ASC
#     LIMIT 5;''')
# query3 = cursor.fetchall()
# cursor.execute('''
#     SELECT COUNT(1) as num_of_students_in_a_room, Room.Id, Room.Name
#     FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
#     GROUP BY Room.Id, Room.Name
#     HAVING COUNT(DISTINCT(Student.Sex)) > 1
# ''')
# query4 = cursor.fetchall()
# print('query1:','\n', query1)
# print('query2:','\n', query2)
# print('query3:','\n', query3)
# print('query4:','\n', query4)


# connection.close()


# # print(students, '\n', rooms)

# # print(test)
