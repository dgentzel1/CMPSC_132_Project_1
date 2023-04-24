# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: LinkedList.py
# Date: 4/30/23
#
# Short Description: Linkedlist ADT

# Import statement
from Node import Node

class LinkedList:

    # Constructor
    def __init__(self):
        self.head = None

    # Add student to linkedlist
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Remove student from linkedlist
    def remove(self, value):
        temp = self.head

        if temp:
            if temp == value:
                self.head = temp.next
                temp = None
                return

        while temp:
            if temp.getData() == value:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None
