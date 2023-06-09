# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Advisor.py
# Date: 4/25/23
#
# Short Description: Store Advisor information
from LinkedList import LinkedList

class Advisor:

    # Constructor
    def __init__(self, fName, mName, lName, title, department, advisees):
        self.__firstName = fName
        self.__middleName = mName
        self.__lastName = lName
        self.__title = title
        self.__department = department
        self.__advisee = advisees

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
        self.__advisee = advisee

    # Advisee accessor
    def getAdvisee(self):
        return self.__advisee

    def print(self):
        return f"{self.__firstName} {self.__middleName} {self.__lastName}\n" \
                 f"Department: {self.__title}\n" \
                 f"Title: {self.__department}\n" \

    # Print advisor information
    def __str__(self):
        s = ''

        # Parse through linkedlist of advisees
        if not self.__advisee:
            s = 'There are no courses to display'
        else:
            c = self.__advisee.head
            while c:
                s += str(f'{c.getData()}\n')
                print(s)
                c = c.next

        result = f"{self.__title} {self.__firstName} {self.__middleName} {self.__lastName}\n" \
                 f"Department: {self.__title}\n" \
                 f"Title: {self.__department}\n" \
                 f"Advisees: {s} \n"

        return result
