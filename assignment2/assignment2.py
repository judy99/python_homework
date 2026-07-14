import csv, traceback
from datetime import datetime

def handle_exception(e):
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")


def read_employees():
    dict = {}
    list = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            first_row = True
            reader = csv.reader(file)
            for row in reader:
                if first_row:
                    dict['fields'] = row
                    first_row = False
                else:
                    list.append(row)
            dict['rows'] = list
        return dict
    except Exception as e:
        handle_exception(e)

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(header_name):
    return employees["fields"].index(header_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    try:
        col_index = employees["fields"].index("first_name")
        res_row = employees["rows"][row_number]
        return res_row[col_index]
    except Exception as e:
        handle_exception(e)

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    sort_field = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[sort_field])
    return employees["rows"]

# Task 8: Create a dict for an Employee
def employee_dict(row):
    keys = employees["fields"]
    dict = {}
    
    for key, item in zip(keys, row):
        if key == "employee_id": continue
        dict[key] = item
    return dict

print(f"Employee dict: {employee_dict(['2', 'David', 'Thornton', '+882 (369)732-4858x56864'])}")

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    all_employees = {}
    keys = list(map(lambda row: row[0], employees["rows"])) # get ids
    for key, row in zip(keys, employees["rows"]):
        all_employees[key] = employee_dict(row)
    return all_employees

# Task 10: Use the os Module
import os
def get_this_value():
    return os.environ.get('THISVALUE')

print(f"env_value: {get_this_value()}")

# Task 11: Creating Your Own Module
import custom_module
def set_that_secret(secret):
    custom_module.set_secret(secret)

set_that_secret("abracadabra")
print(f"now secret is: {custom_module.secret}")

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = {}
    minutes2 = {}
    def read_file(filename, dict):
        try:
            with open(filename, "r", newline="\n") as file:
                reader = csv.reader(file)
                dict["fields"] = next(reader)
                dict["rows"] = list(tuple(row) for row in reader)
            return dict
        except Exception as e:
            handle_exception(e)
    
    read_file("../csv/minutes1.csv", minutes1)
    read_file("../csv/minutes2.csv", minutes2)
    
    return minutes1, minutes2
    
minutes1, minutes2 = read_minutes()

# Task 13: Create minutes_set
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])
    return minutes1_set.union(minutes2_set)

minutes_set = create_minutes_set()

# Task 14: Convert to datetime
def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

minutes_list = create_minutes_list()

# Task 15: Write Out Sorted List
def write_sorted_list():
    header = minutes1["fields"]
    minutes_list.sort(key=lambda item: item[1])
    result = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(result)
    return result

print(write_sorted_list())