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

def print_youngest_employee_info(employees):
  youngest_employee_age = employees[0]["age"]
  youngest_employee_name = employees[0]["name"]
  for employee in employees:
    if employee["age"] < youngest_employee_age:
      youngest_employee_age = employee["age"]
      youngest_employee_name = employee["age"]

  print(f"{youngest_employee_name}")
  print(f"{youngest_employee_age}")


print_youngest_employee_info(employees)
