import random
print("Hello,Welcome to Rock, Paper, Scissors Game")
print("""Rules Of This Game: 
      1.THERE WILL BE 3 ROUNDS 
      2.YOU MUST WIN ATLEAST 2 ROUNDS IN ORDER TO WIN
      3.LOL YOU ARE EXPECTING ME TO EXPLAIN YOU THE RULES OF ROCK,PAPER AND SCISSORS YOU DUMBO
      4.YOU BETTER WIN HUMAN OTHERWISE YOU ARE A BURDEN ON THIS EARTH""")
name = input("Please enter your name: ")
print(f"Let's Start the game {name}")
games = 3
choice = ["Rock","Paper","Scissors"]

user_score = 0
computer_score = 0
for games in range(1,games+1):
  print(f"\nGame {games}:")
  user_move=input("Your Move: ").lower()
  move = random.choice(choice).lower()
  if user_move not in ["rock", "paper", "scissors"]:
    print("Invalid Move,please try again")
    continue
  print(f"Computer's Choice = {move.capitalize()}")
  print(f"{name}'s Choice = {user_move.capitalize()}")
  if user_move == move:
    print("It's A Tie")
  elif (user_move == "scissors" and move == "paper") or \
    (user_move == "rock" and move == "paper") or \
    (user_move == "rock" and move == "scissors"):
    print(f"{name} WON this round!!!")
    user_score += 1
  else:
    print("Computer Won this round!!!")
    computer_score += 1

if(user_score > computer_score):
  print(f"\nCONGRATULATIONS {name} WON!!!")
elif(computer_score > user_score):
  print("\nCOMPUTER WON THIS GAME")
else:
  print("It Was a Tie between the players")

print(f"\nI hope you enjoyed playing this game {name},See You Next Time!!")



  


  
