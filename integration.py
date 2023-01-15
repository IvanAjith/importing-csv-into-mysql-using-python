import pandas as pd        #importing pandas
import mysql.connector as conn  #import sql connector
from mysql.connector import Error

df = pd.read_csv('/Users/ajithsmacbookair/Downloads/Data Science /LMS/Python/Python Notes /datasets/boston.csv')

try:
    connection = conn.connect(host = 'localhost', user ='root', password = '9789861061')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute('USE Car_deko')
        cursor.execute("CREATE TABLE CarData (S_no int(10), crim int(20), zn int(20), indus int(20), chas int(20), nox int(20), rm int(20), age int(20), dis int(20), rad int(20), tax int(20), ptratio int(20), black int(20), Istat int(20), medy int(20))")
        print('Table is created')
        for i,row in df.iterrows():
            sql = "INSERT INTO Car_deko.CarData VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print('Record Inserted')
            connection.commit()
except Error as e:
    print('Error while integration')


# Execute query
sql1  = "SELECT * FROM Car_deko.CarData"
cursor.execute(sql1)
# Fetch all the records
result1 = cursor.fetchall()
for i in result1:
    print(i)


