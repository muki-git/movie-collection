"""This is a simple Rock, Paper Sicssors game written in python. The game is applicable to be run in the CLI for now"""
import random 

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: )")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

#choices = get_choices()

#print(choices)  

def check_win(player, computer):
  print(f"You choose {player}, Computer choose {computer}")
  if player == computer:
    return "It's a tie!"
    
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "paper cover rock! You lose."

   
  elif player == "paper":
    if computer == "rock":
      return "paper covers rock! You win!"
    else:
      return "scissors cuts paper! You lose."

  elif player == "scissors":
    if computer == "paper":
      return "scissors cuts paper! You win!"
    else:
      return "rock smashes scissors! You lose."

      
choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)