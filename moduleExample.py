#!/usr/bin/python

from m1 import displayLocalTime;
from m2 import displayCal;

displayLocalTime()

year=input("Enter year---> ")
month=input("Enter month--> ")
if (year.isdigit()==True & month.isdigit()==True):
    if (int(month)>0 & int(month)<13):
        displayCal(year,month)
    else:
        print("The month is not valid")
else:
    print("Value is not digit")
