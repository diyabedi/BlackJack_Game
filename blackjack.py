import random
import os
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  c=random.choice(cards)
  return c

def calculate_score(cards):
  score=sum(cards)
  if score==21 and len(cards)==2:
    return 0
  if 11 in cards and score>21:
    cards.remove(11)
    cards.append(1)
    
  return score

def compare(user_score,computer_score):
  if user_score==computer_score:
    return "Draw"
  elif computer_score==0:
    return "Lose, opponent has a Blackjack"
  elif user_score==0:
    return "Win with a Blackjack"
  elif user_score>21:
    return "You went over. You lose"
  elif computer_score>21:
    return "Opponent went over. You win"
  elif user_score>computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  user_cards=[]
  computer_cards=[]
  user_score=0
  computer_score=0
  isgameover=False

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not(isgameover):
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      isgameover=True
    else:
      user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal=="y":
        user_cards.append(deal_card())
      else:
        isgameover=True

  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=='y':
  os.system("clear")
  print(logo)
  play_game()




  

  