# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Address.py
# Date: 3/17/23
#
# Short Description: Store address information

class Address:

    # Constructor
    def __init__(self, street='Street', city='City', state='ST', zipcode='*****'):
        self.__strNo = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode

    # Street mutator
    def setStreet(self, street):
        self.__strNo = street

    # Street accessor
    def getStreet(self):
        return self.__strNo

    # City mutator
    def setCity(self, city):
        self.__city = city

    # City accessor
    def getCity(self):
        return self.__city

    # State mutator
    def setState(self, state):
        self.__state = state

    # State accessor
    def getState(self):
        return self.__state

    # Zipcode mutator
    def setZipCode(self, zc):
        self.__zipcode

    # Zipcode accessor
    def getZipCode(self):
        return self.__zipcode

    # Display address information
    def __str__(self):
        return f'{self.__strNo}, {self.__city}, {self.__state} {self.__zipcode}'