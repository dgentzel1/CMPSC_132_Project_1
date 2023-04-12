# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Course.py
# Date: 4/30/23
#
# Short Description: Store Course information

class Course:

    # Constructor
    def __init__(self, number, sem, delivery, status, grade):
        self.number = number
        self.semester = sem
        self.delivery = delivery
        self.status = status
        self.grade = grade

    # Course number mutator
    def setNumber(self, num):
        self.number = num

    # Course number accessor
    def getNumber(self):
        return self.number

    # Semester mutator
    def setSemester(self, semester):
        self.semester = semester

    # Semester accessor
    def getSemester(self):
        return self.semester

    # Delivery method mutator
    def setDelivery(self, delivery):
        self.delivery = delivery

    # Delivery method accessor
    def getDelivery(self):
        return self.delivery

    # Course status mutator
    def setStatus(self, status):
        self.status = status

    # Course status accessor
    def getStatus(self):
        return self.status

    # Grade mutator
    def setGrade(self, grade):
        self.grade = grade

    # Grade accessor
    def getGrade(self):
        return self.grade

    # Print course information
    def __str__(self):
        return f'Course: {self.number}\nSemester: {self.semester}\nDelivery: {self.delivery}\nStatus: {self.status}\nGrade: {self.grade}'
