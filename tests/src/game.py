
def compare_choices(player1_choice, player2_choice):

    if (player1_choice == "rock" and player2_choice == "scissors") or (player1_choice == "scissors" and player2_choice == "paper") or (player1_choice == "paper" and player2_choice == "rock"):
            return "Player 1 Wins!!!"

    if (player2_choice == "rock" and player1_choice == "scissors") or (player2_choice == "scissors" and player1_choice == "paper") or (player2_choice == "paper" and player1_choice == "rock"):
            return "Player 2 Wins!!!"
            
    if (player1_choice == "scissors" and player2_choice == "scissors") or (player1_choice == "paper" and player2_choice == "paper") or (player1_choice == "rock" and player2_choice == "rock"):
            return "It's a draw!!"