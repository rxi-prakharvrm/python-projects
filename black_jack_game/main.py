# from replit import clear
from art import logo
import random

game_over = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
current_score = 0
computer_cards = []
computer_score = 0
another_card = True

want_to_play = input("Do you want to play the blackjack? Type 'y' or 'n': ")

if want_to_play == 'y':
  print(logo)

  your_cards.append(random.choice(cards))
  your_cards.append(random.choice(cards))

  computer_cards.append(random.choice(cards))
  
  current_score = sum(your_cards)
  computer_score = sum(computer_cards)
  
  print(f"Your cards: {your_cards}, current score: {current_score}")
  print(f"Computer cards: {computer_cards}")

  while another_card:
    another_card = input("Do you want to get another card? Type 'y or 'n': ")
    if another_card == 'n':
      computer_cards.append(random.choice(cards))
      computer_score = sum(computer_cards)
      if computer_score < 17:
        computer_cards.append(random.choice(cards)) 
      else:
        print("You Win!")
      another_card == False
      
    your_cards.append(random.choice(cards))
    current_score = sum(your_cards)
    print(f"Your cards: {your_cards}, current score: {current_score}")
    print(f"Computer cards: {computer_cards}")
    
    if sum(your_cards) > 21:
      print("You Lose!")
      another_card = False

    if current_score > computer_score:
      print("You Win!")
      another_card = False
      
    else:
      print("You Lose!")
      another_card = False
      



# game_end = False
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# your_cards = []
# computer_cards = []
# current_score = 0
# computer_score = 0
# another_card = 'y'

# want_to_play = input(
#     "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# while not game_end:
#   if want_to_play == "n":
#     game_end = True
#     break
#   clear()
#   print(logo)

#   your_cards = [random.choice(cards), random.choice(cards)]
#   for card in your_cards:
#     current_score += card

#   print(f"Your cards: {your_cards}, current score: {current_score}")
#   computer_cards = [random.choice(cards)]
#   print(f"Computer's first card: {computer_cards[0]}")

#   if another_card == 'y':
#     another_card = input("Type 'y' to get another card, type 'n' to pass: ")
#     your_cards.append(random.choice(cards))
#     current_score += your_cards.pop()
#     print(f"Your current score: {current_score}")

#     if current_score > 21:
#       print("You Lose!")
#       exit()
#   else:
#     if current_score == computer_score:
#       print("Draw!")
#     elif current_score > computer_score:
#       print("You win!")
#     else:
#       print("You Lose!")

#   if computer_score < 17:
#     computer_cards.append(random.choice(cards))
#     computer_score += computer_cards.pop()

#     if computer_score > 21:
#       print(f"Computer score: {computer_score}")
#       print("You Win!")
#       exit()

#   print(f"Computer score: {computer_score}")

  
