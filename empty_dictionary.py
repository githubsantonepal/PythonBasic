#!/usr/bin/python

#declaring empty dictionary

dict_data={}

#Recoding the values of the in dictionary
for j in range(3):
    name=input('Enter the name ')
    dict_data[j]=name

#displaying the values of the dictionary
for i in dict_data:
    print(i," : ",dict_data[i] )
