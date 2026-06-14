#Create a program that takes a list of student names and stores them in a file. Then, read
#the file and display the contents.

Students=[]
num = int(input("Enter number of students: "))

# Taking input of student names
for i in range(num):
    name = input(f"Enter student name {i+1} : ")
    Students.append(name)

# Writing in file
with open("students.txt", "w") as file:
    for student in Students:
       file.write(f"{student}\n")

#reading from file and printing
with open("students.txt", "r") as file:
    print("List of students names:")
    for line in file:
        print(line.strip())
  
