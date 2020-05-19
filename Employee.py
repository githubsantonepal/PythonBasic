#!/usr/bin/python

class Employee:
    empCount=0

    def __init__(self,empID,name,age,salary):
        self.empID=empID
        self.name=name
        self.age=age
        self.salary=salary
        Employee.empCount=Employee.empCount+1

    def displayDetail(self):
        print("ID : ",self.empID)
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Salary : ",self.salary)


#creating list of Objects
listObj=[]

#creating object of the class Employee

print("*****Employee Information*****")
for i in range(2):
    name=input("Name --> ")
    age=input("Age --> ")
    salary=input("Salary --> ")
    listObj.append(Employee(i,name,age,salary))

print("*****Employee Details*****")
for obj in listObj:
    obj.displayDetail()
    print(".................")

print("Total Employee :: ",Employee.empCount)

