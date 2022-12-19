import mysql.connector
import json

# def db(database_name='db'):
#     return psycopg2.connect(database=database_name)

# def query_db(query, args=(), one=False):
#     cur = db().cursor()
#     cur.execute(query, args)
#     r = [dict((cur.description[i][0], value) \
#             for i, value in enumerate(row)) for row in cur.fetchall()]
#     cur.connection.close()
#     return (r[0] if r else None) if one else r

# def test_query():
#     my_query = query_db('''
#         SELECT COUNT(1) AS Number_of_students, Student.RoomId
#         FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
#         GROUP BY Student.RoomId;
#         ''')
#     jsonString = json.dumps(my_query)
#     jsonFile = open("data.json", "w")
#     jsonFile.write(jsonString)
#     jsonFile.close()

def query_1():
    # establish connection to SQL server
    connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
    print('Database connected, ready to execute the query')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT COUNT(1) AS Number_of_students, Student.RoomId
        FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
        GROUP BY Student.RoomId;
        ''')

    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
            json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

def query_2() -> None:
    # establish connection to SQL server
    connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
    print('Database connected, ready to execute the query')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT Room.Id, AVG(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) AS age
        FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
        GROUP BY Room.Id
        ORDER BY age ASC
        LIMIT 5;
    ''') 

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    connection.close()
    print(result)

def query_3() -> None:
    # establish connection to SQL server
    connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
    print('Database connected, ready to execute the query')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT Room.Id, MAX(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) - MIN(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), str_to_date(Birthday, '%Y-%m-%d'))), '%Y') + 0) AS age
        FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
        GROUP BY Room.Id
        ORDER BY age ASC
        LIMIT 5;
    ''')    

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    connection.close()
    print(result)

def query_4() -> None:
    # establish connection to SQL server
    connection = mysql.connector.connect(user='root', password='root', host='db-server', port = "3306", database = 'db')
    print('Database connected, ready to execute the query')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT COUNT(1) as num_of_students_in_a_room, Room.Id, Room.Name
        FROM Student INNER JOIN Room ON Student.RoomId = Room.Id
        GROUP BY Room.Id, Room.Name
        HAVING COUNT(DISTINCT(Student.Sex)) > 1
    ''')    

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    connection.close()
    print(result)