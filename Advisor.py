# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Advisor.py
# Date: 4/1/23
#
# Short Description: Store Advisor information

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, student):
        new_node = Node(student)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

class Advisor:
    def __init__(self, fName, mName, lName, title, department, advisee):
        self.firstName = fName
        self.middleName = mName
        self.lastName = lName
        self.title = title
        self.department = department
        self.advisee = LinkedList()
        if advisee:
            for student in advisee:
                self.advisee.add_student(student)

    def setFirstName(self, fName):
        self.firstName = fName

    def getFirstName(self):
        return self.firstName

    def setMiddleName(self, mName):
        self.middleName = mName

    def getMiddleName(self):
        return self.middleName

    def setLastName(self, lName):
        self.lastName = lName

    def getLastName(self):
        return self.lastName

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setDepartment(self, department):
        self.department = department

    def getDepartment(self):
        return self.department

    def setAdvisee(self, advisee):
        self.advisee = LinkedList()
        if advisee:
            for student in advisee:
                self.advisee.add_student(student)

    def getAdvisee(self):
        return self.advisee

    def __str__(self):
        result = f"{self.title} {self.firstName} {self.middleName} {self.lastName}\nDepartment: {self.department}\nAdvisee: "
        current = self.advisee.head
        while current:
            result += f'{current.data.firstName} {current.data.lastName}, '
            current = current.next
        return result.rstrip(', ')  # Removes the last comma and space for last in linkedList