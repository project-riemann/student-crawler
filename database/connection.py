import pymysql
connection = pymysql.connect(user='root', passwd='root')

try:
    connection.select_db('students')
except Exception as e:
    ## if error = Unknown database 'students'
    if(e.args[0] == 1049):
        print('create students database')
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE students")
        connection.select_db('students')
    else:
        print(e)