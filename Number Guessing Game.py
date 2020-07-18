#To generate random number in python we will use "random" module
import random
number = random.randint(1, 99)
name_player = input("What is your name.?")
number_of_guess = 0
print("Okay! " + name_player + " Lets play number guessing game, Enter your guess")

while number_of_guess < 5:
    print("Take a Guess")
    guess = int(input())
    number_of_guess = number_of_guess + 1
    if guess < number:
        print("The number is to low")
    if guess > number:
        print("The number is to high")
    if guess == number:
        print("You have guesses the correct number in " + str(number_of_guess) + " tries!")
    else:
        print("you did not guess the number, the number was " + str(number))
