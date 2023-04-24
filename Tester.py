# Name: Christian Ankney and David Gentzel
# Course: CMPSC 132
# File Name: Tester.py
# Date: 4/30/23
#
# Short Description: Use menu to access and manipulate students information

# Import statements
from Address import Address
from Date import Date
from Email import Email
from Phone import Phone
from Semester import Semester
from Student import Student
from Advisor import Advisor
from LinkedList import LinkedList
from Course import Course

# Program output description
print('This program will allow users to add, edit, search, and remove student information.')

# Create student list
student_list = LinkedList()

# Create advisor list
advisor_list = LinkedList()

# Student courses
student1Courses = LinkedList()
student2Courses = LinkedList()
student3Courses = LinkedList()
student4Courses = LinkedList()
student5Courses = LinkedList()

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

# Student course data
student1Course1 = Course('CMPSC 132', 'Spring', 'In Person', 'IP', 'N/A')
student1Course2 = Course('MATH 140', 'Fall', 'Online', 'Completed', 'A')
student1Course3 = Course('CMPSC 221', 'Spring', 'In Person', 'IP', 'N/A')

student1Courses.append(student1Course1)
student1Courses.append(student1Course2)
student1Courses.append(student1Course3)

student2Course1 = Course('BBH 221', 'Fall', 'In Person', 'Completed', 'B')
student2Course2 = Course('MATH 141', 'Spring', 'Online', 'Completed', 'A')
student2Course3 = Course('CMPSC 360', 'Spring', 'In Person', 'IP', 'N/A')

student2Courses.append(student2Course1)
student2Courses.append(student2Course2)
student2Courses.append(student2Course3)

student3Course1 = Course('EE 210', 'Spring', 'In Person', 'IP', 'N/A')
student3Course2 = Course('MATH 140', 'Summer', 'Online', 'Completed', 'C')
student3Course3 = Course('Music 5', 'Fall', 'Hybrid', 'Dropped', 'N/A')

student3Courses.append(student3Course1)
student3Courses.append(student3Course2)
student3Courses.append(student3Course3)

student4Course1 = Course('MATH 230', 'Spring', 'In Person', 'IP', 'D')
student4Course2 = Course('MATH 220', 'Fall', 'Online', 'IP', 'A')
student4Course3 = Course('ART 20', 'Spring', 'In Person', 'IP', 'C')

student4Courses.append(student4Course1)
student4Courses.append(student4Course2)
student4Courses.append(student4Course3)

student5Course1 = Course('PHYS 211', 'Spring', 'In Person', 'Dropped', 'N/A')
student5Course2 = Course('EMCH 211', 'Fall', 'Online', 'Completed', 'A')
student5Course3 = Course('MATH 140', 'Spring', 'In Person', 'IP', 'A')

student5Courses.append(student5Course1)
student5Courses.append(student5Course2)
student5Courses.append(student5Course3)

# Create students
student1 = Student(1, 'John', 'Michael', 'Doe', student1Addresses, student1Emails, student1Phones, student1Birth, student1Acceptance, student1Semester, 'Computer Science', student1Courses)
student2 = Student(2, 'Jane', '', 'Smith', student2Addresses, student2Emails, student2Phones, student2Birth, student2Acceptance, student2Semester, 'Biology', student2Courses)
student3 = Student(3, 'Bob', 'William', 'Johnson', student3Addresses, student3Emails, student3Phones, student3Birth, student3Acceptance, student3Semester, 'Psychology', student3Courses)
student4 = Student(4, 'Samantha', 'M', 'Garcia', student4Addresses, student4Emails, student4Phones, student4Birth, student4Acceptance, student4Semester, 'History', student4Courses)
student5 = Student(5, 'David', 'J', 'Lee', student5Addresses, student5Emails, student5Phones, student5Birth, student5Acceptance, student5Semester, 'English', student5Courses)

# Append students to linkedlist
student_list.append(student1)
student_list.append(student2)
student_list.append(student3)
student_list.append(student4)
student_list.append(student5)

# Create advisor and append to linkedlist
advisor = Advisor('Charles', 'X', 'Helou', 'Advisor', 'Mathematics', student_list)
advisor_list.append(advisor)

# Print menu options
def printMenu():
    choice = int(input('''
    \n Please type the corresponding number for the operation that you would like to perform.

    1 - Add student to list
    2 - Edit student in list
    3 - Delete student from list
    4 - Display information for a student
    5 - Navigate to advisor menu
    6 - Exit\n
    '''))

    return choice

# Print advisor submenu options
def printAdvisorMenu():
    choice = int(input('''
    \n Please type the corresponding number for the operation that you would like to perform.

    1 - Add an advisor
    2 - Display advisor's information with student information
    3 - Edit advisor's information
    4 - Remove student
    5 - Display only advisor's information
    6 - Exit\n
    '''))

    return choice

# Add student to list
def addStudent():

    f1 = 1
    f2 = 1
    f3 = 1
    f4 = 1

    addresses = []
    emails = []
    phones = []
    courses = LinkedList()

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

    # Get course information
    while f4:
        courseNumber = input('Enter course number: ')
        courseSemester = input('Enter course semester: ')
        courseDelivery = input('Please enter delivery method (In Person, Online, or Hybrid): ')

        while courseDelivery != 'In Person' and courseDelivery != 'Online' and courseDelivery != 'Hybrid':
            courseDelivery = input('Please enter one of the three options: ')

        courseStatus = input('Please enter course status (IP, Completed, or Dropped): ')

        while courseStatus != 'IP' and courseStatus != 'Completed' and courseStatus != 'Dropped':
            courseStatus = input('Please enter one of the three options: ')

        courseGrade = input('Enter grade: ')

        while courseGrade != 'A' and courseGrade != 'B' and courseGrade != 'C' and courseGrade != 'D' and courseGrade != 'F' and courseGrade != 'N/A':
            courseGrade = input('Please enter a valid grade: ')

        course = Course(courseNumber, courseSemester, courseDelivery, courseStatus, courseGrade)
        courses.append(course)

        # Ask if user wants to add another course
        f4 = int(input('Would you like to enter another course? Enter 1 for yes and 0 for no. '))
        while f4 != 0 and f4 != 1:
            f4 = int(input('Would you like to enter another course? Enter 1 for yes and 0 for no. '))

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
    student = Student(id, fName, mName, lName, addresses, emails, phones, birthday, acceptanceDate, semester, major, courses)

    # Add student to list
    student_list.append(student)

    # Return to menu
    main()

# Edit student in list
def editStudent(): # Edits a students information

    newCourses = LinkedList()

    id = int(input('Please enter the student ID that you want to manipulate: '))
    found = False

    if not student_list:
        print('There are no students to display.')
        main()
    else:
        student = student_list.head
        while student:
            if student.getData().getID() == id:
                s = student.getData()
                found = True
                print(str(student))  # Prints student information
                print('Please enter new information. Leave blank to keep the previous information.')
                fName = input(f'First name ({s.get_fName()}): ') or s.get_fName()
                mName = input(f'Middle name ({s.get_mName()}): ') or s.get_mName()
                lName = input(f'Last name ({s.get_lName()}): ') or s.get_lName()
                addresses = []

                for i in s.get_address_list():
                    street = input(f'Street ({i.getStreet()}): ') or i.getStreet()
                    city = input(f'City ({i.getCity()}): ') or i.getCity()
                    state = input(f'State ({i.getState()}): ') or i.getState()
                    zip = int(input(f'Zip code ({i.getZipCode()}): ')) or i.getZipCode()
                    type = input(f'Type ({i.getType()}): ') or i.getType()
                    address = Address(street, city, state, zip, type)
                    addresses.append(address)

                emails = []
                for i in s.get_email_list():
                    email = input(f'Email ({i.getEmailAddress()}): ') or i.getEmailAddress()
                    type = input(f'Type ({i.getEmailType()}): ') or i.getEmailType()
                    email = Email(email, type)
                    emails.append(email)

                phones = []
                for i in s.get_phone_list():
                    phone = input(f'Phone ({i.getPhoneNumber()}): ') or i.getPhoneNumber()
                    type = input(f'Type ({i.getPhoneType()}): ') or i.getPhoneType()
                    phone = Phone(phone, type)
                    phones.append(phone)

                if s.getCourse():
                    a = s.getCourse().head
                    while a:
                        number = input(f'Course number ({a.getData().getNumber()}): ') or a.getData().getNumber()
                        semester = input(f'Semester ({a.getData().getSemester()}): ') or a.getData().getSemester()
                        delivery = input(f'Delivery ({a.getData().getDelivery()}): ') or a.getData().getDelivery()
                        while delivery != 'In Person' and delivery != 'Online' and delivery != 'Hybrid':
                            delivery = input('Please enter In Person, Hybrid, or Online. ')
                        status = input(f'Status ({a.getData().getStatus()}): ') or a.getData().getStatus()
                        while status != 'IP' and status != 'Completed' and status != 'Dropped':
                            status = input('Please enter IP, Completed, or Dropped. ')
                        grade = input(f'Grade ({a.getData().getGrade()}): ') or a.getData().getGrade()
                        while grade != 'A' and grade != 'B' and grade != 'C' and grade != 'D' and grade != 'F' and grade != 'N/A':
                            grade = input('Please enter a valid grade. ')

                        c = Course(number, semester, delivery, status, grade)
                        newCourses.append(c)

                        a = a.next

                birthDay = int(
                    input(f'Day of birth ({s.get_birth_date().getDay()}): ')) or s.get_birth_date().getDay()
                birthMonth = int(input(
                    f'Month of birth ({s.get_birth_date().getMonth()}): ')) or s.get_birth_date().getMonth()
                birthYear = int(input(
                    f'Year of birth ({s.get_birth_date().getYear()}): ')) or s.get_birth_date().getYear()
                birthDate = Date(birthDay, birthMonth, birthYear)

                acceptanceDay = int(input(
                    f'Day of acceptance ({s.get_acceptance().getDay()}): ')) or s.get_acceptance().getDay()
                acceptanceMonth = int(input(
                    f'Month of acceptance ({s.get_acceptance().getMonth()}): ')) or s.get_acceptance().getMonth()
                acceptanceYear = int(input(
                    f'Year of acceptance ({s.get_acceptance().getYear()}): ')) or s.get_acceptance().getYear()
                acceptanceDate = Date(acceptanceDay, acceptanceMonth, acceptanceYear)

                term = input(f'Term ({s.get_semester().getTerm()}): ') or s.get_semester().getTerm()
                year = int(input(f'Year ({s.get_semester().getYear()}): ')) or s.get_semester().getYear()
                semester = Semester(term, year)

                major = input(f'Major ({s.get_major()}): ') or s.get_major()

                # Update student information
                s.set_fName(fName)
                s.set_mName(mName)
                s.set_lName(lName)
                s.set_address_list(addresses)
                s.set_email_list(emails)
                s.set_phone_list(phones)
                s.set_birth_date(birthDate)
                s.set_acceptance(acceptanceDate)
                s.set_semester(semester)
                s.set_major(major)
                s.setCourse(newCourses)
                print('Student information updated!')
                main()
            student = student.next

        print(f'No student found with ID:{id}')
        main()  # Return to main menu
    main()

# Delete student from linkedlist
def delStudent():

    # Ask user for ID of student to delete, along with confirmation and validation
    id = int(input('Enter the id of student you want to delete: '))
    option = int(input(f'You have selected student id:{id}, confirm deletion? 1 for yes/0 for no: '))
    while option != 0 and option != 1:
        option = int(input(f'You have selected student id:{id}, confirm deletion? 1 for yes/0 for no: '))

    # Find student and delete information or state that the student was not found
    if option == 1:
        if not student_list:
            print('There are no students to display.')
            main()
        else:
            student = student_list.head
            while student:
                if student.getData().getID() == id:
                    student_list.remove(student)
                    main()
                student = student.next

            print(f'No student found with ID:{id}')
            main()  # Return to main menu
    main()

def displayInformation(student_list): # Display student information

    # Find student with valid ID
    studID = int(input('Enter ID of student for display: '))
    print(f"Searching for student with ID: {studID}")

    # Parse through student linkedlist
    if not student_list:
        print('There are no students to display.')
        main()
    else:
        student = student_list.head
        while student:
            if student.getData().getID() == studID:
                print(student.getData())
                main()
            student = student.next

        print(f'No student found with ID:{studID}')
        main()  # Return to main menu
    main()

# Add advisor to advisor linkedlist
def addAdvisor(student_list):
    advisees = LinkedList()

    f1 = 1

    fName = input('Please enter a first name: ')
    mName = input('Please enter a middle name: ')
    lName = input('Please enter a last name: ')
    title = input('Please enter an advisor title: ')
    department = input('Please enter an advisor department: ')

    addAdvisee = int(input('Would you like to add an advisee? Enter 1 for yes and 0 for no: '))

    while addAdvisee != 0 and addAdvisee != 1:
        addAdvisee = int(input('Would you like to add an advisee? Enter 1 for yes and 0 for no: '))

    # Add advisee if option is chosen
    if addAdvisee == 1:

        while f1:
            specificID = int(input('Is there a specific student you would like to add by ID? Enter 1 for yes and 0 for no: '))
            while specificID != 0 and specificID != 1:
                specificID = int(input('Is there a specific student you would like to add by ID? Enter 1 for yes and 0 for no: '))

            # Add specific student by ID
            if specificID == 1:
                id = int(input('Please enter the ID: '))

                # Parse through student linkedlist
                if not student_list:
                    print('There are no students to display.')
                    main()
                else:
                    student = student_list.head
                    while student:
                        if student.getData().getID() == id:
                            advisees.append(student)
                        student = student.next

            # If no specific ID is chosen, add student manually
            else:
                f1 = 1
                f2 = 1
                f3 = 1
                f4 = 1

                addresses = []
                emails = []
                phones = []
                courses = LinkedList()

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

                # Get course information
                while f4:
                    courseNumber = input('Enter course number: ')
                    courseSemester = input('Enter course semester: ')
                    courseDelivery = input('Please enter delivery method (In Person, Online, or Hybrid): ')

                    while courseDelivery != 'In Person' and courseDelivery != 'Online' and courseDelivery != 'Hybrid':
                        courseDelivery = input('Please enter one of the three options: ')

                    courseStatus = input('Please enter course status (IP, Completed, or Dropped): ')

                    while courseStatus != 'IP' and courseStatus != 'Completed' and courseStatus != 'Dropped':
                        courseStatus = input('Please enter one of the three options: ')

                    courseGrade = input('Enter grade: ')

                    while courseGrade != 'A' and courseGrade != 'B' and courseGrade != 'C' and courseGrade != 'D' and courseGrade != 'F' and courseGrade != 'N/A':
                        courseGrade = input('Please enter a valid grade: ')

                    course = Course(courseNumber, courseSemester, courseDelivery, courseStatus, courseGrade)
                    courses.append(course)

                    # Ask if user wants to add another course
                    f4 = int(input('Would you like to enter another course? Enter 1 for yes and 0 for no. '))
                    while f4 != 0 and f4 != 1:
                        f4 = int(input('Would you like to enter another course? Enter 1 for yes and 0 for no. '))

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
                student = Student(id, fName, mName, lName, addresses, emails, phones, birthday, acceptanceDate,
                                  semester, major, courses)

                # Add student to list
                advisees.append(student)

            f1 = int(input('Would you like to add another advisee? Enter 1 for yes and 0 for no: '))
            while f1 != 1 and f1 != 0:
                f1 = int(input('Would you like to add another advisee? Enter 1 for yes and 0 for no: '))

    advisor = Advisor(fName, mName, lName, title, department, advisees)
    advisor_list.append(advisor)

    main()

# Display advisor with student information
def displayAdvisorAll(advisor_list):

    # Find advisor with valid name
    name = input('Enter first and last name of advisor: ')
    print(f"Searching for advisor: {name}")

    # Parse through linkedlist of advisors
    if not advisor_list:
        print('There are no advisors to display.')
    else:
        advisor = advisor_list.head
        while advisor:
            s = advisor.getData().getFirstName() + ' ' + advisor.getData().getLastName()
            if s == name:
                print(advisor.getData())
                main()
            advisor = advisor.next

        print(f'No advisor found with name: {name}')
        main()

# Edit advisor in advisor linkedlist
def editAdvisor(): #TODO Finish this

    newCourses = LinkedList()

    # Find advisor with valid name
    name = input('Enter first and last name of advisor: ')
    print(f"Searching for advisor: {name}")

    # Parse through advisor linkedlist
    if not advisor_list:
        print('There are no advisors to edit.')
    else:
        advisor = advisor_list.head
        while advisor:
            s = advisor.getData().getFirstName() + ' ' + advisor.getData().getLastName()
            if s == name:
                fName = input(f'First Name ({advisor.getData().getFirstName()}): ') or advisor.getData().getFirstName()
                mName = input(f'Middle Name ({advisor.getData().getMiddleName()}): ') or advisor.getData().getMiddleName()
                lName = input(f'Name ({advisor.getData().getLastName()}): ') or advisor.getData().getLastName()
                title = input(f'Title ({advisor.getData().getTitle()}): ') or advisor.getData().getTitle()
                department = input(f'Department ({advisor.getData().getDepartment()}): ') or advisor.getData().getDepartment()

                # if not advisor.getData().getAdvisee():
                #     print('There are no students to display')
                # else:
                #     advisee = advisor.getData().getAdvisee().head
                #     while advisee:
                #         s = advisee.getData()
                #         found = True
                #         print(str(advisee))  # Prints student information
                #         print('Please enter new information. Leave blank to keep the previous information.')
                #         fName = input(f'First name ({s.get_fName()}): ') or s.get_fName()
                #         mName = input(f'Middle name ({s.get_mName()}): ') or s.get_mName()
                #         lName = input(f'Last name ({s.get_lName()}): ') or s.get_lName()
                #         addresses = []
                #
                #         for i in s.get_address_list():
                #             street = input(f'Street ({i.getStreet()}): ') or i.getStreet()
                #             city = input(f'City ({i.getCity()}): ') or i.getCity()
                #             state = input(f'State ({i.getState()}): ') or i.getState()
                #             zip = int(input(f'Zip code ({i.getZipCode()}): ')) or i.getZipCode()
                #             type = input(f'Type ({i.getType()}): ') or i.getType()
                #             address = Address(street, city, state, zip, type)
                #             addresses.append(address)
                #
                #         emails = []
                #         for i in s.get_email_list():
                #             email = input(f'Email ({i.getEmailAddress()}): ') or i.getEmailAddress()
                #             type = input(f'Type ({i.getEmailType()}): ') or i.getEmailType()
                #             email = Email(email, type)
                #             emails.append(email)
                #
                #         phones = []
                #         for i in s.get_phone_list():
                #             phone = input(f'Phone ({i.getPhoneNumber()}): ') or i.getPhoneNumber()
                #             type = input(f'Type ({i.getPhoneType()}): ') or i.getPhoneType()
                #             phone = Phone(phone, type)
                #             phones.append(phone)
                #
                #         if s.getCourse():
                #             a = s.getCourse().head
                #             while a:
                #                 number = input(
                #                     f'Course number ({a.getData().getNumber()}): ') or a.getData().getNumber()
                #                 semester = input(
                #                     f'Semester ({a.getData().getSemester()}): ') or a.getData().getSemester()
                #                 delivery = input(
                #                     f'Delivery ({a.getData().getDelivery()}): ') or a.getData().getDelivery()
                #                 while delivery != 'In Person' and delivery != 'Online' and delivery != 'Hybrid':
                #                     delivery = input('Please enter In Person, Hybrid, or Online. ')
                #                 status = input(f'Status ({a.getData().getStatus()}): ') or a.getData().getStatus()
                #                 while status != 'IP' and status != 'Completed' and status != 'Dropped':
                #                     status = input('Please enter IP, Completed, or Dropped. ')
                #                 grade = input(f'Grade ({a.getData().getGrade()}): ') or a.getData().getGrade()
                #                 while grade != 'A' and grade != 'B' and grade != 'C' and grade != 'D' and grade != 'F' and grade != 'N/A':
                #                     grade = input('Please enter a valid grade. ')
                #
                #                 c = Course(number, semester, delivery, status, grade)
                #                 newCourses.append(c)
                #
                #                 a = a.next
                #
                #         birthDay = int(
                #             input(f'Day of birth ({s.get_birth_date().getDay()}): ')) or s.get_birth_date().getDay()
                #         birthMonth = int(input(
                #             f'Month of birth ({s.get_birth_date().getMonth()}): ')) or s.get_birth_date().getMonth()
                #         birthYear = int(input(
                #             f'Year of birth ({s.get_birth_date().getYear()}): ')) or s.get_birth_date().getYear()
                #         birthDate = Date(birthDay, birthMonth, birthYear)
                #
                #         acceptanceDay = int(input(
                #             f'Day of acceptance ({s.get_acceptance().getDay()}): ')) or s.get_acceptance().getDay()
                #         acceptanceMonth = int(input(
                #             f'Month of acceptance ({s.get_acceptance().getMonth()}): ')) or s.get_acceptance().getMonth()
                #         acceptanceYear = int(input(
                #             f'Year of acceptance ({s.get_acceptance().getYear()}): ')) or s.get_acceptance().getYear()
                #         acceptanceDate = Date(acceptanceDay, acceptanceMonth, acceptanceYear)
                #
                #         term = input(f'Term ({s.get_semester().getTerm()}): ') or s.get_semester().getTerm()
                #         year = int(input(f'Year ({s.get_semester().getYear()}): ')) or s.get_semester().getYear()
                #         semester = Semester(term, year)
                #
                #         major = input(f'Major ({s.get_major()}): ') or s.get_major()
                #
                #         # Update student information
                #         s.set_fName(fName)
                #         s.set_mName(mName)
                #         s.set_lName(lName)
                #         s.set_address_list(addresses)
                #         s.set_email_list(emails)
                #         s.set_phone_list(phones)
                #         s.set_birth_date(birthDate)
                #         s.set_acceptance(acceptanceDate)
                #         s.set_semester(semester)
                #         s.set_major(major)
                #         s.setCourse(newCourses)
                #         print('Student information updated!')
                #     advisee = advisee.next

            advisor.getData().setFirstName(fName)
            advisor.getData().setMiddleName(mName)
            advisor.getData().setLastName(lName)
            advisor.getData().setTitle(title)
            advisor.getData().setDepartment(department)

            advisor = advisor.next

    main()

# Remove student from an advisor's list of students
def removeStudent():
    pass

# Display advisor without student information
def displayAdvisor():
    # Find advisor with valid name
    name = input('Enter first and last name of advisor: ')
    print(f"Searching for advisor: {name}")

    # Parse through advisor linkedlist
    if not advisor_list:
        print('There are no advisors to display.')
    else:
        advisor = advisor_list.head
        while advisor:
            s = advisor.getData().getFirstName() + ' ' + advisor.getData().getLastName()
            print(s)
            if s == name:
                print(advisor.getData().print())
                main()
            advisor = advisor.next

        print(f'No advisor found with name: {name}')
        main()

def exit():
    pass

# Advisor option menu
def advisorOptions(student_list):

    choice = printAdvisorMenu()

    if choice < 1 or choice > 6:  # Validate valid choice
        main()
    elif choice == 1:  # Add advisor
        addAdvisor(student_list)
    elif choice == 2:  # Display advisors with student information
        displayAdvisorAll(advisor_list)
    elif choice == 3:  # Edit advisor
        editAdvisor()
    elif choice == 4:  # Remove student from advisor
        removeStudent()
    elif choice == 5:  # Display only advisor information
        displayAdvisor()
    elif choice == 6:
        main() # Exit menu

# Main menu options
def main():

    choice = printMenu()

    if choice < 1 or choice > 6:  # Validate valid choice
        main()
    elif choice == 1:  # Add student information
        addStudent()
    elif choice == 2:  # Edit student information
        editStudent()
    elif choice == 3:  # Delete student information
        delStudent()
    elif choice == 4:  # Display student information
        displayInformation(student_list)
    elif choice == 5:  # Navigate to advisor menu
        advisorOptions(student_list)
    elif choice == 6:
        exit()  # Exit program

# Main function
if __name__ == '__main__':
    main()