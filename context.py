
# Number Guessing Game
import random

# Generating a number between 1-100
correct_guess = random.randint(1, 100)

attempt = 0

print("Welcome to the Number Guessing Game!")
print("Let's start the game!")

while True:
    try:
        guess = int(input("Enter your guess number: "))
        attempt += 1


        if attempt==5:
          print("GAME OVER")
          break

        if guess < 1 or guess > 100:
            print("Enter a number between 1-100")

        elif guess < correct_guess:
            print("Your guess is too low!")

        elif guess > correct_guess:
            print("Your guess is too high!")

        else:
            print(f"You guessed the right number! It was {correct_guess}.")
            print(f"You got the correct number in {attempt} attempts.")
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")
