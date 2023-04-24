# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Node.py
# Date: 4/30/23
#
# Short Description: Create node for linkedlist implementation

class Node:

    # Constructor
    def __init__(self, data):
        self.__data = data
        self.next = None

    # Data mutator
    def setData(self, data):
        self.__data = data

    # Data accessor
    def getData(self):
        return self.__data

    # Print node data
    def __str__(self):
        return f'{self.__data}'