import pandas as pd        #importing pandas
import mysql.connector as conn  #import sql connector
from mysql.connector import Error

try:   #Using exception to log errors
    connection = conn.connect(host = 'localhost', user = 'root', password = '9789861061')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute('create database Car_deko')              #Uing sql queries, Im creating a database
        print('Database is created')
except Error as e:
    print('Error while connecting')