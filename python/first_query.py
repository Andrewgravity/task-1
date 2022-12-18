def query_1():
    import mysql.connector

    # establish connection to SQL server
    connection = mysql.connector.connect(user='root', password='root', host='mysql', port = "3306", database = 'db')
    print('Database connected, ready to execute the first query')

    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(1), rooms.ROOM_NAME FROM students INNER JOIN rooms ON students.ROOM = rooms.ROOM_ID GROUP BY students.ROOM')
    test = cursor.fetchall()
    connection.close()
    print(test)