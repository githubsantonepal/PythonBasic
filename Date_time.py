#!/usr/bin/python

import time;        #required this module to include time
import calendar;    #required this module to include calender
import sys;

#user defined function to display local time
def displayLocalTime():
    localtime=time.asctime(time.localtime(time.time()))
    print("The local time:: ", localtime)
    return;
#user defined function to display calender
def displayCal(year,month):
    cal=calendar.month(int(year),int(month))
    print(cal)
    return;

#Calling function without passing and passing argument

displayLocalTime();

year=input("Enter years less or equals to 2020-->> ")
month=input("Enter month value between 1-12-->> ")
if (year.isdigit()==True) & (month.isdigit()==True):
    if (int(month)>0) & (int(month)<13):
        displayCal(year,month)
    else:
        print("enter valid month")
else:
    print("It is not a digit")









