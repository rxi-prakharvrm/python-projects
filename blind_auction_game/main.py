from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("\nWelcome to the secret auction program.\n")

volunteers = {}
is_any_other_bidder = True

while is_any_other_bidder:
  volunteer_name = input("What's your name?: ")
  bid_money = int(input("What's your bid?: $"))
  volunteers[volunteer_name] = bid_money

  result = input("Are there any other bidders? Type 'yes' or 'no'.")

  if result == "no":
    is_any_other_bidder = False
  clear()

highest_bid = 0
highest_bidder = ""

for volunteer in volunteers:
  if volunteers[volunteer] > highest_bid:
    highest_bid = volunteers[volunteer]
    highest_bidder = volunteer
    
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")