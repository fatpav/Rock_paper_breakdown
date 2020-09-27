class Game():
        def compare_choices(self, player1, player2):

                if (player1.choice == "rock" and player2.choice == "scissors") or (player1.choice == "scissors" and player2.choice == "paper") or (player1.choice == "paper" and player2.choice == "rock"):
                        return "Player 1 Wins!!!"
                        

                if (player2.choice == "rock" and player1.choice == "scissors") or (player2.choice == "scissors" and player1.choice == "paper") or (player2.choice == "paper" and player1.choice == "rock"):
                        return "Player 2 Wins!!!"
                        
                        
                if (player1.choice == "scissors" and player2.choice == "scissors") or (player1.choice == "paper" and player2.choice == "paper") or (player1.choice == "rock" and player2.choice == "rock"):
                        return "It's a draw!!"
                        