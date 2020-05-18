#!/usr/bin/python

import calendar;

def displayCal(year,month):
    cal=calendar.month(int(year),int(month))
    print(cal)
    return;