# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Email.py
# Date: 4/25/23
#
# Short Description: Store email information

class Email:

    # Constructor
    def __init__(self, emailAddress='user@email.com', emailType='(Type)'):
        self.__email_address = emailAddress
        self.__email_type = emailType

    # Email address mutator
    def setEmailAddress(self, emailAddress):
        self.__email_address = emailAddress

    # Email address accessor
    def getEmailAddress(self):
        return self.__email_address

    # Email type mutator
    def setEmailType(self, emailType):
        self.__email_type = emailType

    # Email type accessor
    def getEmailType(self):
        return self.__email_type

    # Display email information
    def __str__(self):
        return f'{self.__email_address} ({self.__email_type})'

