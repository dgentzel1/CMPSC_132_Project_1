# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Semester.py
# Date: 3/17/23
#
# Short Description: Store semester information

class Semester:

    # Constructor
    def __init__(self, term:'season', year:0000):
        self.__term = term
        self.__year = year

    # Term mutator
    def setTerm(self, term):
        self.__term = term

    # Term accessor
    def getTerm(self):
        return self.__term

    # Year mutator
    def setYear(self, year):
        self.__year = year

    # Year accessor
    def getYear(self):
        return self.__year

    # Display semester information
    def __str__(self):
        return f'{self.__term} {self.__year}'