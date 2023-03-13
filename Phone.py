# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Phone.py
# Date: 3/17/23
#
# Short Description: Store phone information

class Phone:

    # Constructor
    def __init__(self, phoneNumber='(###)-###-####', phoneType='(Type)'):
        self.__phone_number = phoneNumber
        self.__phone_type = phoneType

    # Phone number mutator
    def setPhoneNumber(self, phoneNumber):
        self.__phone_number = phoneNumber

    # Phone number accessor
    def getPhoneNumber(self):
        return self.__phone_number

    # Phone type mutator
    def setPhoneType(self, phoneType):
        self.__phone_type = phoneType

    # Phone number accessor
    def getPhoneType(self):
        return self.__phone_type

    # Display phone information
    def __str__(self):
        return f'Phone: {self.__phone_number} {self.__phone_type}'

