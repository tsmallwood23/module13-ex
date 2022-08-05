calculation_count = 0
while True:
    num1 = input(f"hi, input a number\n")
    if num1 == "exit":
        print("exiting the program")
        print(f"Thanks for calculating, you did {calculation_count} calculations!")
        break
    elif num1 != "exit":
        num2 = input(f"hi, input a 2nd number\n")
        oper = input(f"hi, input an operator\n")
        valid_numbers = num1.isdigit() and num2.isdigit()
        valid_oper = oper == "+" or oper == "/" or oper == "*" or oper == "-"
        if not valid_numbers:
            print("not a valid number, try again")
        elif not valid_oper:
            print("not a valid operator, try again")
        else:
            print("Calculating...")
            calculation_count = calculation_count + 1
            if oper == "+":
                print(int(num1) + int(num2))
            elif oper == "-":
                print(int(num1) - int(num2))
            elif oper == "/":
                print(int(num1) / int(num2))
            elif oper == "*":
                print(int(num1) * int(num2))