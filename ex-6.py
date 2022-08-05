import random
random_number = (random.randint(1,9))


print("Welcome to my random number guessing game.")

while True:
    user_guess = input("Give it a go and guess your number!\n")
    if int(user_guess) == random_number:
        print("Congrats! You guessed right. Here is your prize\n :)")
        break
    elif int(user_guess) > random_number:
        print("Too high! Try again")
    elif int(user_guess) < random_number:
        print("Too low. Try again!")
