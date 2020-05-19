#!/usr/bin/python

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
#geocoder is used to know the specific location of the number

x=input("Enter the phone number with country code")
if (phonenumbers.is_valid_number(x))==True:
    phoneNumber=phonenumbers.parse(x,None)
    print(phoneNumber)

    #this will print the country name
    print(geocoder.description_for_number(phoneNumber, 'en'))

    #this will print the service provider name
    print(carrier.name_for_number(phoneNumber, 'en'))
else:
    print("Not a valid number")