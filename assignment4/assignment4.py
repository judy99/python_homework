import pandas as pd
# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# Add a new column
salary = pd.DataFrame({'Salary': [70000, 80000, 90000]})
task1_with_salary = task1_data_frame.copy()
task1_with_salary = task1_with_salary.join(salary)
print(task1_with_salary)

# Modify an existing column
task1_older = task1_with_salary.copy()
age_series = task1_older['Age'].copy()
age_series = age_series.apply(lambda x: x + 1)
task1_older['Age'] = age_series
print(task1_older)

# Save the DataFrame as a CSV file
task1_older.to_csv("employees.csv", index=False)

# Task 2: Loading Data from CSV and JSON
# Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print(f"\nRead data from a CSV file: \n{task2_employees}")

# Read data from a JSON file
json_employees = pd.read_json('additional_employees.json')
print(f"\nRead data from a JSON file: \n{json_employees}")

# Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(f"\nCombine DataFrames: \n{more_employees}")

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# Use the head(), tail() methods
first_three = more_employees.head(3)
print(f"\nFirst three: \n{first_three}")

last_two = more_employees.tail(2)
print(f"\nLast two: \n{last_two}")

#  Get the shape of a DataFrame
employee_shape = more_employees.shape
print(f"\nShape of a DataFrame: \n{employee_shape}")

# Use the info() method
print(f"\n{more_employees.info()}")

#  Task 4: Data Cleaning
dirty_data = pd.read_csv('dirty_data.csv')
print(f"\nRead data from a dirty_data file: \n{dirty_data}")

clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
clean_data["Age"] = clean_data["Age"].fillna(1)
print(f"\nclean_data Age: \n{clean_data}")

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], "NaN")
print(f"\nclean_data Salary: \n{clean_data}")

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
mean_age = clean_data["Age"].mean()
median_salary = clean_data["Salary"].median()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print(f"\nclean_data mean/median: \n{clean_data}")

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format='mixed', errors="coerce")
print(f"\nclean_data Date: \n{clean_data}")

clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()
print(f"\nclean_data standardize: \n{clean_data}")

