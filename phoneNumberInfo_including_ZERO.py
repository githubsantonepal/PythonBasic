#!/usr/bin/python

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
#geocoder is used to know the specific location of the number

x=input("Enter the phone number with country code")
if x.isdigit()==True:
    phoneNumber=phonenumbers.parse(x,"GB")
    print(phoneNumber)

    #this will print the country name
    print("Number Used in",geocoder.description_for_number(phoneNumber, 'en'))

    # #this will print the service provider name
    print("Service Provider",carrier.name_for_number(phoneNumber, 'en'))
else:
    print("Number is not a digit")