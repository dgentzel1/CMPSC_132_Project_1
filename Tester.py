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
from Student import Student

# Program output description
print('This program will allow users to add, edit, search, and remove student information.')

# TODO populate with 5 members
# Create student list
student_list = []

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

    f1 = 1
    f2 = 1
    f3 = 1

    addresses = []
    emails = []
    phones = []

    id = int(input('Student ID: '))
    fName = input('Student first name: ')
    mName = input('Student middle name: ')
    lName = input('Student last name: ')

    while f1:
        street = input('Student street address: ')
        city = input('Student city: ')
        state = input('Student state: ')
        zip = input('Student zip code: ')

        address = Address(street, city, state, zip)
        addresses.append(address)

        # TODO add validation
        f1 = int(input('Would you like to enter another address? Enter 1 for yes and 0 for no. '))

    while f2:
        email = input('Student email address: ')
        emailType = input('Student email type: ')

        email = Email(email, emailType)
        emails.append(email)

        # TODO add validation
        f2 = int(input('Would you like to enter another email? Enter 1 for yes and 0 for no. '))

    while f3:
        phone = input('Student phone number: ')
        phoneType = input('Student phone type: ')

        phone = Phone(phone, phoneType)
        phones.append(phone)

        # TODO add validation
        f3 = int(input('Would you like to enter another phone? Enter 1 for yes and 0 for no. '))

    birthDay = int(input('Student day of birth: '))
    birthMonth = int(input('Student month of birth: '))
    birthYear = int(input('Student year of birth: '))
    acceptanceDay = int(input('Student day of acceptance: '))
    acceptanceMonth = int(input('Student month of acceptance: '))
    acceptanceYear = int(input('Student year of acceptance: '))
    term = input('Student semester: ')
    termYear = int(input('Student term year: '))
    major = input('Student intended major: ')

    birthday = Date(birthDay, birthMonth, birthYear)
    acceptanceDate = Date(acceptanceDay, acceptanceMonth, acceptanceYear)
    semester = Semester(term, termYear)

    # Student creation
    student = Student(id, fName, mName, lName, addresses, emails, phones, birthday, acceptanceDate, semester, major)

    # Add student to list
    student_list.append(student)

    # Return to menu
    main()

# Edit student in list
def editStudent():

    id = int(input('Please enter the student ID: '))

    # TODO if id in studentList.getid():

# Display student information
def displayInformation():

    # Find student

    # Print student information
    print(student_list[0])

    # Return to main menu
    main()

def main():

    choice = printMenu()

    if choice < 1 or choice > 5:  # Validate valid choice
        main()
    elif choice == 1:  # Add student information
        addStudent()
    elif choice == 2:  # Edit student information
        pass
    elif choice == 3:  # Delete student information
        pass
    elif choice == 4:  # Display student information
        displayInformation()
    else:
        pass  # Exit program

if __name__ == '__main__':
    main()