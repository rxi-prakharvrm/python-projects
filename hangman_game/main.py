# importing files
import random
from replit import clear
from hangman_art import logo, stages, win, lose
import hangman_words

selected_list = input("Select a word list - \n1. mix_list, 2. animal_list\n")

if selected_list == '1':
  word_list = hangman_words.mix_list
elif selected_list == '2':
  word_list = hangman_words.animal_list

# choose a random word from the word list and make it lowercased
chosen_word = random.choice(word_list).lower()

# finding the length of the randomly chosen word
chosen_word_length = len(chosen_word)

# defining and initializing an empty display list and lives
display = []
lives = 6
single_instance_list = []
end_of_game = False

# appending '-' in the display list up to the length of randomly chosed word
for i in range(chosen_word_length):
  display.append("_")

# printing for the first time before clearing the screen
print(logo)
print("Total lives: 6\n")

# underlying logic behind hangman game
while not end_of_game:
  guessed_letter = input("\nGuess the letter: ")

  # to clear the screen
  clear()

  # printing logo again after clearing the screen
  print(logo)

  # checking if the letter already guessed or not
  if guessed_letter in single_instance_list:
    print(stages[lives])
    print("Already guessed!")
    continue
    
  else:
    # appending every letter of the randomly chosen word without repeating it
    single_instance_list.append(guessed_letter)

  # decreasing lives by 1 if none instance of the guessed_letter is present in it
  if guessed_letter not in chosen_word:
    lives -= 1
    
  # alternative way of decreasing lives by 1 if none instance of the guessed_letter is present in it
  """
  if chosen_word.find(guessed_letter) == -1:
    lives -= 1  
  """

  # changing underscore by guessed letter in display list if it is in the chosed word
  for i in range(chosen_word_length):
    if guessed_letter == chosen_word[i]:
      display[i] = guessed_letter

  # printing things
  print(stages[lives])
  print("\n" + ''.join(display))
  print(f"\nLives remained: {lives}")

  # checking whether there are any remained underscores if not just print win
  if "_" not in display:
    end_of_game = True
    print(win)

  # checking for the lives if there is no life then print lose
  if lives == 0:
    end_of_game = True
    print("\n==========================\n")
    print("The word was: " + chosen_word)
    print("\n==========================")
    print(lose)