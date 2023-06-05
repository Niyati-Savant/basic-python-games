
import random

flag=False
logo = """ 
    _   __                __                 ______                     _            
   / | / /_  ______ ___  / /_  ___  _____   / ____/_  _____  __________(_)___  ____ _
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / / __/ / / / _ \/ ___/ ___/ / __ \/ __ `/
 / /|  / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __(__  |__  ) / / / / /_/ / 
/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      \____/\__,_/\___/____/____/_/_/ /_/\__, /  
                                                                            /____/
      """

print(logo)
num = random.randint(1, 100)
print("Welcome to the Number Guessing Game")
print("I am guessing a number between 1 to 100")
print(f"A secret between you and me :) --> Sol is: {num}")
level=int(input("Choose a difficulty level: easy(0) or hard(1):"))

if level==0:
  attempts=10
elif level==1:
  attempts=5
else:
    print("Invalid Level Number.Exit")
    attempts=0

while(attempts !=0):
  print(f"You have {attempts} attempts left")
  guess=int(input("Make a guess: "))

  if (guess==num):
    flag=True
    break
  else:
    attempts-=1
    if guess<num:
      print("Too low")
    else :
      print("Too High")

if (level ==0 or level ==1):
    if (flag):
        print("Congratulations !! You won")
    else:
        print(f"Sorry :( Out of attempts.The solution was {num}")
