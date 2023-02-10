import os

class Game:

    def __init__(self):
        self.launched = True
        self.combo = {
            "stone": "paper",
            "paper": "cisor",
            "cisor": "stone"
        }

    # get value of variable in class
    def get(self, want):

        if want == "launch":
            return self.launched
        if want == "combo":
            return self.combo
        
        ValueError("Invalid argument")

    # set value of variable in class
    def set(self, want, value):

        if want == "launch":
            self.launched = value
        
        ValueError("Invalid argument")

    # check who have win the round
    def round_winner(self, players):

        if self.combo[players[0].get("choice")] == players[1].get("choice"):
            player = players[1]
        elif self.combo[players[1].get("choice")] == players[0].get("choice"):
            player = players[0]
        else:
            player = None

        return player

    # check if have winner
    def winner(self, players):

        if players[0].get("score") == 3:
            self.set("launch", False)
            current = players[0].get("name")
        elif players[1].get("score") == 3:
            self.set("launch", False)
            current = players[1].get("name")
        else:
            current = None

        return current

    # print the score of players
    def print(self, players):

        os.system("cls")
        msg = "\n"
        for player in players:
            msg += f"{player.get('name')}: {player.get('score')}\n"

        print(msg)

    def __repr__(self) -> str:
        return "An instance of the game is launch"