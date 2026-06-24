"""
Program Name: Match Coins Game
Author: Chris Martinez
Purpose: This class manages the game itself like the game loop and declaring who the winner is
Starter Code: N/A
Date: June 23, 2026
"""

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print("Player 1 has " + str(player1.get_wallet()))
    print("Player 2 has " + str(player2.get_wallet()))

    user_input = input("Do you want to toss the coins? (y/n): ")

    while user_input == "y" or user_input == "Y":

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print("Tossing...")

        print("Player 1 tossed " + side1)
        print("Player 2 tossed " + side2)

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("Its a Match! Player 1 wins a coin.")
        else:
            player1.lose_coin()
            player2.win_coin()
            print("No Match! Player 2 wins a coin.")

        print("Player 1 has " + str(player1.get_wallet()) + " coins.")
        print("Player 2 has " + str(player2.get_wallet()) + " coins.")

        user_input = input("Do you want to toss the coins? (y/n): ")

    print("--- Final Score ---")
    print("Player 1: " + str(player1.get_wallet()))
    print("Player 2: " + str(player2.get_wallet()))

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 has more coins!")

    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 has more coins!")
    else:
        print("It's a draw!")    
           
        
if __name__ == "__main__":
    main()
            



