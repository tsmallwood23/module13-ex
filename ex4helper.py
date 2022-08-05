employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]
employees2 = [{
  "name": "Bob",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

def print_youngest_employee_info(employees):
  youngest_employee_age = employees[0]["age"]
  youngest_employee_name = employees[0]["name"]
  for employee in employees:
    if employee["age"] < youngest_employee_age:
      youngest_employee_age = employee["age"]
      youngest_employee_name = employee["age"]

  print(f"{youngest_employee_name}")
  print(f"{youngest_employee_age}")

def string_calc(string):
  lower_letters = 0
  upper_letters = 0
  for char in list(string):
    if char.islower():
      lower_letters += 1
    elif char.isupper():
      upper_letters +=1


  print(f"lower is {lower_letters}")
  print(f"upper is {upper_letters}")


def even_count(list):
  for number in list:
    if number % 2 == 0:
      print(number)