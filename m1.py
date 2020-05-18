#!/usr/bin/python

import time;


#user defined function to display local time
def displayLocalTime():
    localtime=time.asctime(time.localtime(time.time()))
    print("The local time:: ", localtime)
    return;