def get_choices():
 player = input("rock, paper or scissors? ")
 computer = random.choice(["rock", "paper", "scissors"])
 return {"player": player, "computer": computer} # dictionary of both
def check_win(player, computer):
 print(f"You chose {player}, computer chose {computer}")
 if player == computer:
 return "It's a tie!"
 elif player == "rock":
 return "You win!" if computer == "scissors" else "You lose!"
 elif player == "paper":
 return "You win!" if computer == "rock" else "You lose!"
 elif player == "scissors":
 return "You win!" if computer == "paper" else "You lose!"
choices = get_choices()
print(check_win(choices["player"], choices["computer"]))
