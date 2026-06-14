''' Implement a program to store student records (name, roll, marks,contact number) using a
dictionary.
a. Provide menu options to add, search, and display students
'''
Students={}
#Method for add function
def add():
    roll=input("Enter rollno of the sutdent: ")
    name=input("Enter name of the student: ")
    marks=input("Enter marks of the student: ")
    contact=input("Enter contact number of the student: ")
    Students[roll]={
        'Name':name,
        'Marks':marks,
        'Contact':contact
    }

#method for search function
def search():
    roll=input("Enter rollno to search: ")

    if roll in Students:
        print("Student found.")
        print("RollNo: ",roll)
        print("Name: ", Students[roll]["Name"])
        print("Marks: ",Students[roll]["Marks"])
        print("Contact Number: ", Students[roll]["Contact"])
    else:
        print("Entered rollno does not exist.")

#method for display
def display():
    if len(Students)==0:
        print("No records found.")
    else:
        print("Displaying all Students: ")
        for roll,details in Students.items():
            print("RollNo: ",roll)
            print("Name: ", details["Name"])
            print("Marks: ",details["Marks"])
            print("Contact Number: ", details["Contact"])
            print()

#main menu
while True:
    print("Student Records::")
    print("1. Add")
    print("2. Search")
    print("3. Display")
    print("4. Exit")
    choise= input("Enter your choise: ")

    if choise == "1":
        add()
    elif choise == "2":
        search()
    elif choise =="3":
        display()
    elif choise =="4":
        print("Eciting Program.....")
        break
    else:
        print("Invalid choise! please try again.")