# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Student.py
# Date: 4/25/23
#
# Short Description: Store and display student information

# Node class for linkedlist

class Student:

    # Constructor
    def __init__(self, id=0, fName='', mName='', lName='', addr=[], email=[], phone=[], birthdate=None, acceptance=None, semester=None, major='', courses=None):
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
        self.__course_list = courses

    # ID mutator
    def setID(self, ID):
        self.__id = ID

    # ID accessor
    def getID(self):
        return self.__id

    # Mutator/accessor for First Name
    def get_fName(self):
        return self.__fName
    def set_fName(self, fName):
        self.__fName = fName

    # Mutator/accessor for Middle Name
    def get_mName(self):
        return self.__mName
    def set_mName(self, mName):
        self.__mName = mName

    # Mutator/accessor for Last Name
    def get_lName(self):
        return self.__lname
    def set_lName(self, lName):
        self.__lname = lName

    # Mutator/accessor for address list
    def get_address_list(self):
        return self.__address_list
    def set_address_list(self, addr):
        self.__address_list = addr

    # Mutator/accessor for email list
    def get_email_list(self):
        return self.__email_list
    def set_email_list(self, email):
        self.__email_list = email

    # Mutator/accessor for phone_list
    def get_phone_list(self):
        return self.__phone_list
    def set_phone_list(self, phone):
        self.__phone_list = phone

    # Mutator/accessor for birth_date
    def get_birth_date(self):
        return self.__birth_date
    def set_birth_date(self, birthdate):
        self.__birth_date = birthdate

    # Mutator/accessor for acceptance
    def get_acceptance(self):
        return self.__acceptance
    def set_acceptance(self, acceptance):
        self.__acceptance = acceptance

    # Mutator/accessor for semester
    def get_semester(self):
        return self.__semester
    def set_semester(self, semester):
        self.__semester = semester

    # Mutator/accessor for major
    def get_major(self):
        return self.__major
    def set_major(self, major):
        self.__major = major

    def setCourse(self, course):
        self.__course_list = course

    def getCourse(self):
        return self.__course_list

    # Display student information
    def __str__(self):
        addresses = self.__address_list
        emails = self.__email_list
        phones = self.__phone_list
        s = ''

        # Parse through linkedlist of courses
        if not self.__course_list:
            s = 'There are no courses to display'
        else:
            c = self.__course_list.head
            while c:
                s += str(f'{c.getData()}\n')
                print(s)
                c = c.next

        return f'\nID: {self.__id} \n' \
               f'Name: {self.__fName} {self.__mName} {self.__lname} \n' \
               f'Addresses: {", ".join(str(i) for i in addresses)} \n' \
               f'Emails: {", ".join(str(i) for i in emails)} \n' \
               f'Phones: {", ".join(str(i) for i in phones)} \n' \
               f'Birth date: {self.__birth_date} \n' \
               f'Acceptance date: {self.__acceptance} \n' \
               f'Semester: {self.__semester} \n' \
               f'Intended major: {self.__major} \n' \
               f'Courses: {s} \n'