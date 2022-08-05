my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]

#step 1
"""for number in my_list:
    if number >= 10:
        print(number)"""

#step 2
"""new_list = []
for number in my_list:
    if number >= 10:
        new_list.append(number)
    else:
        ""
print(new_list)"""

#step 3
new_list = []
user_input = input(f"enter one number\n")
int_user_input = int(user_input)

for number in my_list:
    if number > int_user_input:
        new_list.append(number)
    else:
        ""
print(new_list)
