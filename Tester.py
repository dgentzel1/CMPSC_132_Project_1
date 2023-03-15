# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Tester.py
# Date: 3/17/23
#
# Short Description: Use menu to access and manipulate students information

# Import statements
from Address import Address
from Date import Date
from Email import Email
from Phone import Phone
from Semester import Semester

# Program output description
print('This program will allow users to add, edit, search, and remove student information.')

# Print menu options
def printMenu():
    choice = int(input('''
    \n Please type the corresponding number for the operation that you would like to perform.

    1 - Add student to list
    2 - Edit student in list
    3 - Delete student from list
    4 - Display information for a student
    5 - Exit
    '''))

    return choice

# Add student to list
def addStudent():

    id = int(input('Student ID: '))
    fName = input('Student first name: ')
    mName = input('Student middle name: ')
    lName = input('Student last name: ')
    street = input('Student street address: ')
    city = input('Student city: ')
    state = input('Student state: ')
    zip = input('Student zip code: ')
    email = input('Student email address: ')
    emailType = input('Student email type: ')
    phone = input('Student phone number: ')
    phoneType = input('Student phone type: ')
    birthDay = int(input('Student day of birth: '))
    birthMonth = int(input('Student month of birth: '))
    birthYear = int(input('Student year of birth: '))
    acceptanceDay = int(input('Student day of acceptance: '))
    acceptanceMonth = int(input('Student month of acceptance: '))
    acceptanceYear = int(input('Student year of acceptance: '))
    term = input('Student semester: ')
    termYear = int(input('Student term year: '))
    major = input('Student intended major: ')

    address = Address(street, city, state, zip)
    email = Email(email, emailType)
    phone = Phone(phone, phoneType)
    birthday = Date(birthDay, birthMonth, birthYear)
    acceptanceDate = Date(acceptanceDay, acceptanceMonth, acceptanceYear)
    semester = Semester(term, termYear)

    # add student creation

def main():

    choice = printMenu()

    if choice < 1 or choice > 5:  # Validate valid choice
        main()
    elif choice == 1:  # Add student information
        pass
    elif choice == 2:  # Edit student information
        pass
    elif choice == 3:  # Delete student information
        pass
    elif choice == 4:  # Display student information
        pass
    else:
        pass  # Exit program

if __name__ == '__main__':
    main()