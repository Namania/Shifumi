import random

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = ""


    # get value of variable in class
    def get(self, want):

        if want == "name":
            return self.name
        if want == "score":
            return self.score
        if want == "choice":
            return self.choice
        
        ValueError("Invalid argument")

    # set value of variable in class
    def set(self, want, choice):

        if want == "name":
            self.name = choice
        if want == "score":
            self.score = choice
        if want == "choice":
            self.choice = choice
        
        ValueError("Invalid argument")

    # add value at player score
    def add(self, count):
        self.score += count

    # player a random choice (only for computer)
    def play(self, choices):
        return choices[random.randint(0, 2)]

    def __repr__(self) -> str:
        return f'Player {self.name} was successfully created and his score is: {self.score}'