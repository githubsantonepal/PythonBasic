#!/usr/bin/python3
import time
import mysql.connector
class DatabaseConnection:
    def __init__(self, mydatabase):
        try:
            global mycursor
            global mydb
            self.databasename=mydatabase
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="NiceNepal@123!",
                database=self.databasename
            )
            print("You are Connected to "+self.databasename+" Database")
            mycursor=mydb.cursor()
            time.sleep(3)
        except:
            print("Database does not exits")
            exit()

    def createTable(self):
        #try:
            pass
            #tablename
            #mycursor.execute("CREATE TABLE ")

        #except:

    def dropTable(self):
        pass

    def showTables(self):
        mycursor.execute("SHOW TABLES")
        print("****Tables in the Database****")
        for i in mycursor:
            print(i)

    def alterTable(self):
        # ADDING EXTRA KEY FOR THE TABLE WITH PRIMARY KEY
        mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

    def insertValue(self):
        pass

    def selectValue(self):
        pass

    def deleteValue(self):
        pass

    def updateValue(self):
        pass
print("Options:")
print("C: To Connect with Database")
print("I: To Ignore Database Connectivity")
response=input("Make the Selection from Above Options--> ")
if(response.lower().strip()=='c'):
    #try:
    mydatabase = input("Enter the database to Connect")
    db = DatabaseConnection(mydatabase)
    response=''
    while response!='q':
        print("MENU")
        print("1. To Create Table")
        print("2. To Drop Table")
        print("3. To Show Tables")
        print("4. To Alter Tables")
        print("5. To Insert Values in the Tables")
        print("6. To Access Values from Table")
        print("7. To Delete Record from Table")
        print("8. To Update Record from Table")
        print("q. To quite the program")

        response = input("Select option from Above-->  ")
        print(response)

        if response.strip()=='1':
            db.createTable()

        elif response.strip()=='2':
            db.dropTable()

        elif response.strip()=='3':
            db.showTables()

        elif response=='4':
            db.alterTable()

        elif response=='5':
            db.insertValue()

        elif response=='6':
            db.selectValue()

        elif response=='7':
            db.deleteValue()

        elif response=='8':
            db.updateValue()

        elif response.lower()=='q':
            print("Thanks for Using the software")
            exit()

        else:
            print("You have entered unknown Characters, try enter valid input")
    #except:
        #print(" The database does not exist.")

elif response.lower()=='i':
    print("You have ignore connectivity")
else:
    print("You enter unrecognized characters")




