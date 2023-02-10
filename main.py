from player import Player
from game import Game
import time
import os

os.system("cls")

# initialize game and ask name of players
game = Game()
players = [Player(input("Player name -> ")), Player(input("Computer name -> "))]
winner = None

os.system("cls")

# game
while game.get("launch"):

    # print the score of players
    game.print(players)

    # ask the player choice and chose choice for computer
    players[0].set("choice", input("Choose between stone/paper/cisor: "))
    # if player want to exit
    if players[0].get("choice") == "stop":
        print()
        os._exit(0)
    # if player choice is not valid
    if players[0].get("choice") in list(game.get("combo").keys()):
        players[1].set("choice", players[1].play(list(game.get("combo").keys())))
        print(f"{players[1].get('name')} choice: {players[1].get('choice')}")

        # check who win the round and add 1 at winner score. if have equality, restart the round
        current_player = game.round_winner(players)
        if current_player == None:
            print("\nEquality..")
        else:
            current_player.add(1)

        time.sleep(2.0)

        # check if one of players win the game
        winner = game.winner(players)
    
    # message if player choice is not valid
    else:
        msg = ""
        for element in list(game.get("combo").keys()):
            msg += f"{element}, "
        msg = msg[:-2]
        print(f"\n Invalid input, retry with {msg}")

        time.sleep(2.0)


# End part, print the players score and the winner
game.print(players)
print(f"Le gagant est {winner}\n")