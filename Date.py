# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Date.py
# Date: 3/17/23
#
# Short Description: Store information regarding the date

class Date:

    # Constructor
    def __init__(self, day=00, month=00, year=0000):
        self.__day = day
        self.__month = month
        self.__year = year

    # Day mutator
    def setDay(self, day):
        self.__day = day

    # Day accessor
    def getDay(self):
        return self.__day

    # Month mutator
    def setMonth(self, month):
        self.__month = month

    # Month accessor
    def getMonth(self):
        return self.__month

    # Year mutator
    def setYear(self, year):
        self.__year = year

    # Year accessor
    def getYear(self):
        return self.__year

    # Display date information
    def __str__(self):
        return f'{self.__month}/{self.__day}/{self.__year}'

