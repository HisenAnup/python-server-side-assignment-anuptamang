#Write Python code to read from a CSV file of student marks and calculate average marks

import csv

total_marks = 0

data = {
    "name": "Alex",
    "web": 60,
    "dsa": 75,
    "graphic": 85
}

with open("data.csv", "w", newline = '') as file:
    header = ['name', 'web', 'dsa', 'graphic']
    writing = csv.DictWriter(file, fieldnames=header)
    writing.writeheader()
    writing.writerow(data)
    
with open("data.csv", "r") as file:
    reading = csv.DictReader(file)
    for row in reading:
        print(f"{row['name']} {row['web']} {row['dsa']} {row['graphic']}")
        total_marks = int(row['dsa']) + int(row['graphic']) + int(row['web'])
        
average_mark = total_marks / 3;

print(f"Total mark = {total_marks} and Average mark = {round(average_mark)}")

