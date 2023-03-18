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

# Create student list
student_list = []

# Populate with 5 example students

# Student addresses
student1Addresses = [Address('123 Main St', 'Houston', 'Montana', 15213)]
student2Addresses = [Address('456 Elm St', 'Philadelphia', 'Colorado', 17234)]
student3Addresses = [Address('324 Spruce St', 'Los Angeles', 'Pennyslvania', 16312)]
student4Addresses = [Address('321 Pine St', 'New Orleans', 'Delaware', 13241)]
student5Addresses = [Address('654 Cedar St', 'Seattle', 'California', 12345)]

# Student emails
student1Emails = [Email('johndoe@example.com', 'Personal')]
student2Emails = [Email('janesmith@example.com', 'Personal')]
student3Emails = [Email('bob@example.com', 'Personal'), Email('bwilliam@example.com', 'Work')]
student4Emails = [Email('samantha@example.com', 'Personal')]
student5Emails = [Email('davidlee@example.com', 'Personal')]

# Student phones
student1Phones = [Phone('610-555-1234', 'Mobile')]
student2Phones = [Phone('610-555-5678', 'Mobile')]
student3Phones = [Phone('610-555-9012', 'Mobile'), Phone('610-555-3456', 'Work')]
student4Phones = [Phone('610-555-7890', 'Mobile')]
student5Phones = [Phone('610-555-2345', 'Mobile')]

# Student birth dates
student1Birth = Date(1, 1, 2001)
student2Birth = Date(2, 2, 2002)
student3Birth = Date(3, 3, 2003)
student4Birth = Date(4, 4, 2004)
student5Birth = Date(5, 5, 2005)

# Student acceptance dates
student1Acceptance = Date(9, 1, 2022)
student2Acceptance = Date(9, 1, 2022)
student3Acceptance = Date(15, 1, 2023)
student4Acceptance = Date(15, 1, 20023)
student5Acceptance = Date(9, 1, 2022)

# Student semester data
student1Semester = Semester('Fall', 2022)
student2Semester = Semester('Fall', 2022)
student3Semester = Semester('Spring', 2023)
student4Semester = Semester('Spring', 2023)
student5Semester = Semester('Fall', 2022)

# Create students
student_list.append(Student(1, 'John', 'Michael', 'Doe', student1Addresses, student1Emails, student1Phones, student1Birth, student1Acceptance, student1Semester, 'Computer Science'))
student_list.append(Student(2, 'Jane', '', 'Smith', student2Addresses, student2Emails, student2Phones, student2Birth, student2Acceptance, student2Semester, 'Biology'))
student_list.append(Student(3, 'Bob', 'William', 'Johnson', student3Addresses, student3Emails, student3Phones, student3Birth, student3Acceptance, student3Semester, 'Psychology'))
student_list.append(Student(4, 'Samantha', 'M', 'Garcia', student4Addresses, student4Emails, student4Phones, student4Birth, student4Acceptance, student4Semester, 'History'))
student_list.append(Student(5, 'David', 'J', 'Lee', student5Addresses, student5Emails, student5Phones, student5Birth, student5Acceptance, student5Semester, 'English'))


# Print menu options
def printMenu():
    choice = int(input('''
    \n Please type the corresponding number for the operation that you would like to perform.

    1 - Add student to list
    2 - Edit student in list
    3 - Delete student from list
    4 - Display information for a student
    5 - Exit\n
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

    # Get address information
    while f1:
        street = input('Student street address: ')
        city = input('Student city: ')
        state = input('Student state: ')
        zip = input('Student zip code: ')
        type = input('Student address type: ')

        address = Address(street, city, state, zip, type)
        addresses.append(address)

        # Ask if user wants to add another address and validate
        f1 = int(input('Would you like to enter another address? Enter 1 for yes and 0 for no. '))
        while f1 != 0 and f1 != 1:
            f1 = int(input('Would you like to enter another address? Enter 1 for yes and 0 for no. '))

    # Get email information
    while f2:
        email = input('Student email address: ')
        emailType = input('Student email type: ')

        email = Email(email, emailType)
        emails.append(email)

        # Ask if user wants to add another email and validate
        f2 = int(input('Would you like to enter another email? Enter 1 for yes and 0 for no. '))
        while f2 != 0 and f2 != 1:
            f2 = int(input('Would you like to enter another email? Enter 1 for yes and 0 for no. '))

    # Get phone information
    while f3:
        phone = input('Student phone number: ')
        phoneType = input('Student phone type: ')

        phone = Phone(phone, phoneType)
        phones.append(phone)

        # Ask if user wants to add another phone and validate
        f3 = int(input('Would you like to enter another phone? Enter 1 for yes and 0 for no. '))
        while f3 != 0 and f3 != 1:
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
def editStudent(): # Edits a students information

    id = int(input('Please enter the student ID that you want to manipulate: '))
    found = False
    for student in student_list:
        print(f"Checking student with ID:{student.getID()}")
        if student.getID() == id:
            found = True
            print(str(student))  # Prints student information
            print('Please enter new information. Leave blank to keep the previous information.')
            fName = input(f'First name ({student.get_fName()}): ') or student.get_fName()
            mName = input(f'Middle name ({student.get_mName()}): ') or student.get_mName()
            lName = input(f'Last name ({student.get_lName()}): ') or student.get_lName()
            addresses = []

            for i in student.get_address_list():
                street = input(f'Street ({i.getStreet()}): ') or i.getStreet()
                city = input(f'City ({i.getCity()}): ') or i.getCity()
                state = input(f'State ({i.getState()}): ') or i.getState()
                zip = int(input(f'Zip code ({i.getZipCode()}): ')) or i.getZipCode()
                type = input(f'Type ({i.getType()}): ') or i.getType()
                address = Address(street, city, state, zip, type)
                addresses.append(address)

            emails = []
            for i in student.get_email_list():
                email = input(f'Email ({i.getEmailAddress()}): ') or i.getEmailAddress()
                type = input(f'Type ({i.getEmailType()}): ') or i.getEmailType()
                email = Email(email, type)
                emails.append(email)

            phones = []
            for i in student.get_phone_list():
                phone = input(f'Phone ({i.getPhoneNumber()}): ') or i.getPhoneNumber()
                type = input(f'Type ({i.getPhoneType()}): ') or i.getPhoneType()
                phone = Phone(phone, type)
                phones.append(phone)

            birthDay = int(input(f'Day of birth ({student.get_birth_date().getDay()}): ')) or student.get_birth_date().getDay()
            birthMonth = int(input(f'Month of birth ({student.get_birth_date().getMonth()}): ')) or student.get_birth_date().getMonth()
            birthYear = int(input(f'Year of birth ({student.get_birth_date().getYear()}): ')) or student.get_birth_date().getYear()
            birthDate = Date(birthDay, birthMonth, birthYear)

            acceptanceDay = int(input(f'Day of acceptance ({student.get_acceptance().getDay()}): ')) or student.get_acceptance().getDay()
            acceptanceMonth = int(input(f'Month of acceptance ({student.get_acceptance().getMonth()}): ')) or student.get_acceptance().getMonth()
            acceptanceYear = int(input(f'Year of acceptance ({student.get_acceptance().getYear()}): ')) or student.get_acceptance().getYear()
            acceptanceDate = Date(acceptanceDay, acceptanceMonth, acceptanceYear)

            term = input(f'Term ({student.get_semester().getTerm()}): ') or student.get_semester().getTerm()
            year = int(input(f'Year ({student.get_semester().getYear()}): ')) or student.get_semester().getYear()
            semester = Semester(term, year)

            major = input(f'Major ({student.get_major()}): ') or student.get_major()

            # Update student information
            student.set_fName(fName)
            student.set_mName(mName)
            student.set_lName(lName)
            student.set_address_list(addresses)
            student.set_email_list(emails)
            student.set_phone_list(phones)
            student.set_birth_date(birthDate)
            student.set_acceptance(acceptanceDate)
            student.set_semester(semester)
            student.set_major(major)
            print('Student information updated!')
            main()
    if not found:
        print(f'No student found with ID:{id}')
        main()  # Return to main menu

def delStudent():

    # Ask user for ID of student to delete, along with confirmation and validation
    id = int(input('Enter the id of student you want to delete: '))
    option = int(input(f'You have selected student id:{id}, confirm deletion? 1 for yes/0 for no: '))
    while option != 0 and option != 1:
        option = int(input(f'You have selected student id:{id}, confirm deletion? 1 for yes/0 for no: '))

    # Find student and delete information or state that the student was not found
    if option == 1:
        print(f'Deleting student with id:{id}')
        for i, student in enumerate(student_list):
            if student.getID() == id:
                del student_list[i]
                print(f'Student with id {id} has been deleted.')
                main() # Return to main menu
        print(f'No student with ID:{id} found, returning to menu.')
    else:
        pass
        main()

def displayInformation(student_list): # Display student information

    # Find student with valid ID
    studID = int(input('Enter ID of student for display: '))
    print(f"Searching for student with ID:{studID}")
    for student in student_list:
        print(f"Checking student with ID:{student.getID()}")
        if student.getID() == studID:
            print(str(student)) # Print student information
            main() # Return to main menu
    print(f'No student found with ID:{studID}')
    main() # Return to main menu

def main():

    choice = printMenu()

    if choice < 1 or choice > 5:  # Validate valid choice
        main()
    elif choice == 1:  # Add student information
        addStudent()
    elif choice == 2:  # Edit student information
        editStudent()
    elif choice == 3:  # Delete student information
        delStudent()
    elif choice == 4:  # Display student information
        displayInformation(student_list)
    else:
        pass # Exit program

if __name__ == '__main__':
    main()