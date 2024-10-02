# Blackjack game.

import random
from replit import clear
from art import logo

def deal_card():
  """deals a random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(
      cards) == 2:  #blackjack if sum is 21 and length is 2
    return 0
  elif sum(cards) > 21 and 11 in cards:  #if sum is 21 and there is an ace in the list, change the ace to 1
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(computer_score, user_score):
"""Compare user score to computer score and print result of the match"""
  if (computer_score == user_score):
    print("It's a draw!")
  elif (computer_score == 0):
    print("You lose! The opponent has Blackjack")
  elif (user_score == 0):
    print("You win! You have a Blackjack")
  elif (user_score > 21):
    print("You lose! Youre score is over 21")
  elif (user_score > computer_score and user_score < 22):
    print("You win! Your score is higher than the opponent")
  elif (computer_score > 21 and user_score < 21):
    print("You win! Youre opponents score is over 21")
  elif ((computer_score > user_score and computer_score < 22)):
    print("you loose! Youre opponents score is higher than you")
  elif (computer_score == 21):
    print("You loose! Your opponents score is 21")

def play_Blackjack():
  
  print(logo) # aschii art, not included
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  #deal two cards to both user and computer
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  user_cards_score = 0
  computer_cards_score = 0
  while not is_game_over:
    user_cards_score = calculate_score(user_cards)
    computer_cards_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score {user_cards_score}")
    print(f"Computer's first card: {computer_cards[0]}")
  
    if (user_cards_score == 0 or computer_cards_score == 0
        or user_cards_score > 21):
      is_game_over = True
    else:
      user_should_deal = input(
          "Do you want another card? Type 'y' or 'n': ")
      if (user_should_deal.lower() == "y"):
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_cards_score != 0 and computer_cards_score < 17:
    computer_cards.append(deal_card())
    computer_cards_score = calculate_score(computer_cards)
  print(f"your final hand: {user_cards}, final score: {user_cards_score}")
  print(f"Your opponents final hand: {computer_cards}, final score: {computer_cards_score}") 
  compare(computer_cards_score,user_cards_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_Blackjack()