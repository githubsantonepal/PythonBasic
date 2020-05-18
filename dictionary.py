#!/usr/bin/python

dict_data={101:'Santosh', 102:'Parbati', 103:'Arya', 104:'Sarita'}
for i in dict_data:
    print(dict_data[i])

#changing the values of key in dictionary
for j in dict_data:
    name=input('Enter the name ')
    dict_data[j]=name

for i in dict_data:
    print(i)
    print(dict_data[i])