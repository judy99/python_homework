# Task 3: List Comprehensions Practice
import csv
with open("../csv/employees.csv", "r", newline="") as file:
     reader = csv.reader(file)
     lists = list(list(row) for row in reader)
print(lists)

employee_names = [f"{item[1]} {item[2]}" for item in lists[1:]]
print(employee_names)

employee_names_with_e = [name for name in employee_names if "e" in name]
print(employee_names_with_e)