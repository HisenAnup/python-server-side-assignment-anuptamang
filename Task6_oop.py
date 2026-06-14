#Develop a simple OOP-based Python class Student with attributes like name, roll
#number, and marks. Implement methods to input and display details.

class Students:
    
    def Getdata(self):
        self.name = input("Enter the name of the student: ")
        self.roll = input("Emter rollno of student: ")
        self.marks = input("Enter marks of the student: ")

    def Display(self):
        print("Name: ", self.name)
        print("Rollno: ", self.roll)
        print("Marks: ",self.marks)


std = Students()
std.Getdata()
std.Display()
