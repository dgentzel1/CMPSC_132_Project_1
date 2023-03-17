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
student_list.append(Student(1, 'John', 'Michael', 'Doe', ['123 Main St', 'Apt 2B'], ['johndoe@example.com Personal'], ['610-555-1234 Mobile'], '2001-01-01', '2022-09-01', 'Fall 2022', 'Computer Science'))
student_list.append(Student(2, 'Jane', '', 'Smith', ['456 Elm St', 'Apt 3C'], ['janesmith@example.com Personal'], ['610-555-5678 Mobile'], '2002-02-02', '2022-09-01', 'Fall 2022', 'Biology'))
student_list.append(Student(3, 'Bob', 'William', 'Johnson', ['789 Oak St', 'Apt 4D'], ['bob@example.com Personal', 'bwilliam@example.com Work'], ['610-555-9012 Mobile', '610-555-3456 Work'], '2003-03-03', '2023-01-15', 'Spring 2023', 'Psychology'))
student_list.append(Student(4, 'Samantha', 'M', 'Garcia', ['321 Pine St', 'Apt 5E'], ['samantha@example.com Personal'], ['610-555-7890 Mobile'], '2004-04-04', '2023-01-15', 'Spring 2023', 'History'))
student_list.append(Student(5, 'David', 'J', 'Lee', ['654 Cedar St', 'Apt 6F'], ['davidlee@example.com Personal'], ['610-555-2345 Mobile'], '2005-05-05', '2022-09-01', 'Fall 2022', 'English'))


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
            addresses = input(f'Addresses ({", ".join(str(i) for i in student.get_address_list())}): ')
            if not addresses:
                addresses = student.get_address_list()
            else:
                addresses = [address.strip() for address in addresses.split(',')]
            emails = input(f'Emails ({", ".join(str(i) for i in student.get_email_list())}): ')
            if not emails:
                emails = student.get_email_list()
            else:
                emails = [email.strip() for email in emails.split(',')]
            phones = input(f'Phone numbers ({", ".join(str(i) for i in student.get_phone_list())}): ')
            if not phones:
                phones = student.get_phone_list()
            else:
                phones = [phone.strip() for phone in phones.split(',')]
            birthDate = input(f'Birth date ({student.get_birth_date()}): ') or student.get_birth_date()
            acceptanceDate = input(f'Acceptance date ({student.get_acceptance()}): ') or student.get_acceptance()
            semester = input(f'Semester ({student.get_semester()}): ') or student.get_semester()
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
    # TODO validate both id and option
    id = int(input('Enter the id of student you want to delete: '))
    option = int(input(f'You have selected student id:{id}, confirm deletion? 1 for yes/0 for no: '))
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