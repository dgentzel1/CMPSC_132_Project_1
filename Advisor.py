# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Advisor.py
# Date: 4/30/23
#
# Short Description: Store Advisor information

# Node class for linkedlist

from LinkedList import LinkedList

class Advisor:

    # Constructor
    def __init__(self, fName, mName, lName, title, department, advisee):
        self.__firstName = fName
        self.__middleName = mName
        self.__lastName = lName
        self.__title = title
        self.__department = department
        self.__advisee = LinkedList()

    # First name mutator
    def setFirstName(self, fName):
        self.__firstName = fName

    # First name accessor
    def getFirstName(self):
        return self.__firstName

    # Middle name mutator
    def setMiddleName(self, mName):
        self.__middleName = mName

    # Middle name accessor
    def getMiddleName(self):
        return self.__middleName

    # Last name mutator
    def setLastName(self, lName):
        self.__lastName = lName

    # Last name accessor
    def getLastName(self):
        return self.__lastName

    # Title mutator
    def setTitle(self, title):
        self.__title = title

    # Title accessor
    def getTitle(self):
        return self.__title

    # Department mutator
    def setDepartment(self, department):
        self.__department = department

    # Department accessor
    def getDepartment(self):
        return self.__department

    # Advisee mutator
    def setAdvisee(self, advisee):
        self.__advisee = LinkedList()
        if advisee:
            for student in advisee:
                self.__advisee.append(student)

    # Advisee accessor
    def getAdvisee(self):
        return self.__advisee

    # Print advisor information
    def __str__(self):
        result = f"{self.__title} {self.__firstName} {self.__middleName} {self.__lastName}\nDepartment: {self.__department}\nAdvisee: "
        current = self.__advisee.head
        while current:
            result += f'{current.data.firstName} {current.data.lastName}, '
            current = current.next
        return result.rstrip(', ')  # Removes the last comma and space for last in linkedList