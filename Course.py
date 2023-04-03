# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Course.py
# Date: 4/1/23
#
# Short Description: Store Course information

class Course:
    def __init__(self, number, sem, delivery, status, grade):
        self.number = number
        self.semester = sem
        self.delivery = delivery
        self.status = status
        self.grade = grade

    def setNumber(self, num):
        self.number = num

    def getNumber(self):
        return self.number

    def setSemester(self, semester):
        self.semester = semester

    def getSemester(self):
        return self.semester

    def setDelivery(self, delivery):
        self.delivery = delivery

    def getDelivery(self):
        return self.delivery

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def setGrade(self, grade):
        self.grade = grade

    def getGrade(self):
        return self.grade

    def __str__(self):
        return f'Course: {self.number}\nSemester: {self.semester}\nDelivery: {self.delivery}\nStatus: {self.status}\nGrade: {self.grade}'
