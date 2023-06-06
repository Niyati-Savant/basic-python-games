from art import logo
from art import vs
from game_data import data
from random import randint
#from replit import clear
import os



def details(x):
  print(f"{data[x]['name']},a {data[x]['description']},from {data[x]['country']} .")

def max_follower(A,B):
  if(data[A]['follower_count']>data[B]['follower_count']):
    return 'A'
  else:
    return 'B'

user_score=0
game_over=False

player_a=randint(0,50)
player_b=randint(0,50)
if player_a==player_b:
  player_b +=1

while(game_over!=True):
  print(logo)
  if(user_score>0):
      print(f"You are right ! Current Score is {user_score}")
    
  print("Comapre A:")
  details(player_a)
  print(vs)
  print("Against B:")
  details(player_b)
  print()
  
  favourite=max_follower(player_a,player_b)
  #print(f"{favourite} has more followers")
  
  user_guess=input("Guess who has more followers, A or B? ").upper()
  
  if user_guess==favourite:
    user_score +=1

    if favourite=='A':
      player_b=randint(0,50)

    elif favourite=='B':
      player_a=player_b
      player_b=randint(0,50)
      
    if player_a==player_b:
      player_b +=1 
    #clear()
    os.system('cls')

  else:
    #clear()
    os.system('cls')
    print(logo)
    print(f"Sorry!Wrong Guess.Final score is: {user_score}")
    game_over=True
    break
    
  
