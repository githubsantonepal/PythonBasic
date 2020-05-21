#!/usr/bin/python3
import time
import mysql.connector
import os

class DatabaseConnection:
    def __init__(self):
        global mydb
        global mycursor
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="NiceNepal@123!"
        )
        time.sleep(2)
        # creating the variable to perform create, drop and show databases
        mycursor = mydb.cursor()

        return


    def statusDatabase(self):
    #prints status of connection between mysql server and  client
        print(mydb)
        return

    def displayExistDatabase(self):
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)

    def createDatabase(self):
        try:
            dbname=input("Enter the Name for database")
            mycursor.execute("CREATE DATABASE "+dbname)
            print("You have created the database " +dbname)
        except:
            print("Database Name already exist, Try Different Name")

    def dropDatabase(self):
        try:
            dropdb=input("Enter the Name of database to Drop")
            mycursor.execute("DROP DATABASE "+dropdb)
            print("You have dropped the database "+dropdb)
        except:
            print("Database does not exist")
    def menuPrint(self):
    #prints Menu
        global response
        print("1: To Create Database")
        print("2. To Drop Database")
        print("3. To Show Databases")
        response=input("What do you want to do?")

db=DatabaseConnection()
response =''
while response !='q':
    db.menuPrint()
    os.system('clear')
    if response=='1':
        db.createDatabase()
    elif response=='2':
        db.dropDatabase()
    elif response=='3':
        db.displayExistDatabase()
    elif response.lower()=='q':
        print("Thank you for using Application, Good BYE")
        exit()
    else:
        print("I do not understand the choice you made, Try Again")


