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
for employee in employees:
  print(f"name: {employee['name']}")
  print(f"name: {employee['job']}")
  print(f"name: {employee['address']['city']}")
  print(f"name: {employee['age']}")
  print("\n")


#wrong print(employees(1, {['address']['country']}))
country = employees[1] ['address']['country']
print(country)
