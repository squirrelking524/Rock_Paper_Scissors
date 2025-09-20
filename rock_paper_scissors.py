import random

print("Let's play rock, paper, scissors")
print("Rules are simple: rock beats scissors, scissors cut paper, and paper covers rock")
print("Game will play till best of three.")

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    player_choice = input("\nPlayer: choose rock, paper, or scissors: ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice =random.choice(choices)
    print(f"Computer choose: {computer_choice}")

    if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        winner = "Player"
    elif (player_choice == computer_choice):
        winner = "Tie"
    else:
        winner = "Computer"

    if winner == "Player":
        player_wins += 1
        print("You won!")
    elif winner == "Computer":
        computer_wins += 1
        print("Computer wins!")
    else:
        print("It's a tie! Go again.")
    
    print(f"Current Score -- Player: {player_wins} and Computer {computer_wins}.")

if player_wins > computer_wins:
    print("Congratulations! Player wins!")
print("So sorry, computer wins!")