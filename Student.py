# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Student.py
# Date: 3/17/23
#
# Short Description: Store and display student information

class Student:

    # Constructor
    def __init__(self, id=0, fName='', mName='', lName='', addr=[], email=[], phone=[], birthdate=None, acceptance=None, semester=None, major=''):
        self.__id = id
        self.__fName = fName
        self.__mName = mName
        self.__lname = lName
        self.__address_list = addr
        self.__email_list = email
        self.__phone_list = phone
        self.__birth_date = birthdate
        self.__acceptance = acceptance
        self.__semester = semester
        self.__major = major

    # ID mutator
    def setID(self, ID):
        self.__id = ID

    # ID accessor
    def getID(self):
        return self.__id

    # TODO add other getters and setters

    # Display student information
    def __str__(self):
        addresses = self.__address_list
        emails = self.__email_list
        phones = self.__phone_list
        return f'\nID: {self.__id} \n' \
               f'Name: {self.__fName} {self.__mName} {self.__lname} \n' \
               f'Addresses: {", ".join(str(i) for i in addresses)} \n' \
               f'Emails: {", ".join(str(i) for i in emails)} \n' \
               f'Phones: {", ".join(str(i) for i in phones)} \n' \
               f'Birth date: {self.__birth_date} \n' \
               f'Acceptance date: {self.__acceptance} \n' \
               f'Semester: {self.__semester} \n' \
               f'Intended major: {self.__major} \n'