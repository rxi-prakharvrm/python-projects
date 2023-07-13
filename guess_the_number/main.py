from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

# If difficulty level is easy attemps = 10 otherwise attemps = 5
if level.lower() == "easy":
  attempts = 10
else:
  attempts = 5

# Printing the left attempts
print(f"You have {attempts} attempts remaining to guess the number.")

# Choosing a random number between 1 and 100
number = random.randint(1, 100)

is_game_over = False

while not is_game_over:
  if attempts == 0:
    print("You've run out of guesses, you lose.")
    is_game_over = True
  else:
    guessed_number = int(input("Make a guess: "))
    
    # if number is less than the number print too low and decrease number of attemps by 1 and let the user guess it again
    if guessed_number < number:
      attempts -= 1
      print("Too low.")
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")  
    
    # if number is greater than the number print too high and decrease number of attemps by 1  and let the user guess it again
    elif guessed_number > number:  
      attempts -= 1
      print("Too high.")
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.") 
      
    # if number is equals to the guessed_num the print you win
    elif guessed_number == number:
      print(f"You got it! the answer was {number}")
      is_game_over = True