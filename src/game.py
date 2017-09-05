
class Move:

    def beats(self, other):
        if other.name in self.winsOver:
            return True
        return False
    
class Lizard(Move):
    def __init__(self):
        self.name = "lizard"
        self.winsOver = ("scissors", "rock", "paper")

class Rock(Move):
    def __init__(self):
        self.name = "rock"
        self.winsOver = ("scissors", )

class Paper(Move):
    def __init__(self):
        self.name = "paper"
        self.winsOver = ("rock", )

class Scissors(Move):
    def __init__(self):
        self.name = "scissors"
        self.winsOver = ("paper", )

MOVES = {
          "rock": Rock,
          "scissors": Scissors,
          "paper": Paper,
          "lizard": Lizard
          }

def create(moveName):
   return MOVES[moveName]()

class RockPaperScissorsGame:

    def beats(self, first, second):
        first = create(first)
        second = create(second)
        return first.beats(second)
