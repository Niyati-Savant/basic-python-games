import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  chosen=random.choice(cards)
  return chosen

def calculate_score(card_list):
  score=0
  for i in card_list:
    score+=i
  if score==21 and len(card_list)==2:
    return 0 #bj
  if 11 in card_list and score>21:
        card_list.remove(11)
        card_list.append(1)
  return score

def compare(user,comp):
  if user==comp:
    print("DRAW")
  elif comp==0: 
    print("YOU LOSE.Computer has BlackJack")
  elif user>21:
    print("YOU LOSE.Your Score over 21")
  elif user==0:
    print("YOU WIN.Got a BlackJack")
  elif comp>21 and comp !=0: 
    print("YOU WIN.Dealer Score over 21")
  else:
    if(user>comp):
      print("YOU WIN with higher score")
    else:
      print("YOU Lose with lesser score")
      
def play_game():
  is_over=False
  user_list=[]
  dealer_list=[]

  for i in range(2):
    user_list.append(deal_card())
    dealer_list.append(deal_card())
  
  while not is_over: 
    """While user wants to play"""
    user_score=calculate_score(user_list)
    dealer_score=calculate_score(dealer_list)
    print(f"User cards-{user_list} and score is {user_score}")
    print(f"Dealer first card-{dealer_list[0]} ")
    
    if user_score==0 or dealer_score==0 or user_score>21:
      is_over=True
    else:
      choice=input("To get another card press y ? ")
      if choice=='y' or choice=='Y':
        user_list.append(deal_card())
      else:
        is_over=True
      
  while(dealer_score !=0 and dealer_score < 17):
    x=deal_card()
    dealer_list.append(x)
    dealer_score+=x
  
  print(f"Final hand User cards-{user_list} and score is {user_score}")
  print(f"Final hand Dealer card-{dealer_list} and score is {dealer_score}")
  
  compare(user_score,dealer_score)

play=input("Press Y to play Blackjack: ")
while(play=='y'or play=='Y'):
  play_game()
  play=input("New Game?")