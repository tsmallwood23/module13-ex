"""employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}"""

#step 1
"""employee["job"] = "Software Engineer"
print(employee)"""

#step 2
"""employee.pop("age")
print(employee)"""

#step 3
"""for key, value in employee.items():
  print(f"{key}:{value}")

employee.items()"""

#step 4
dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}
dict_three = {**dict_one, **dict_two}

#print(dict_three)

#step 5
"""sum = 0
for value in dict_three.values():
  sum = sum + value
print(sum)"""

#step 6
merged_values_list = []
for value in dict_three.values():
    merged_values_list.append(value)

merged_values_list.sort()
print(merged_values_list)
print(f"min value: {merged_values_list[0]}")
print(f"max value: {merged_values_list[len(merged_values_list)-1]}")



