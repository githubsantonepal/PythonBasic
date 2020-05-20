#!/usr/bin/python3
import time
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="NiceNepal@123!"
)

print(mydb)

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase2")

time.sleep(3)

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
