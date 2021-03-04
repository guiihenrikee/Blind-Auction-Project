from replit import clear
from art import *
print (logo)
print("Welcome to the auction!")
auction = {}
new_bid = True
while new_bid == True:
  name = input("Type your name: \n")
  bid = int(input("Type your bid $:"))
  auction[name] = bid
  new_bidder = input("Is there any other bidder? Type 'yes' or 'no'.\n").lower()
  if new_bidder == "yes":
    clear()
    new_bid = True
  else:
    clear()
    new_bid = False
winner = max(auction, key=auction.get)
value = auction.values()
max_value = max(value)
print(f"The winner is {winner} with a bid of {max_value}!")

