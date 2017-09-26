import random
from itertools import cycle

def get_player_names():
    names = []
    while True:
        value = input("Player {}'s name: ".format(len(names) + 1))
        if not value:
            break
        names.append(value)
    return names


class Pig:


    def __init__(self, *players):
        self.players = players
        self.scores = dict.fromkeys(self.players ,0)

    def get_players(self):
        return (self.players)

    def roll(self):
        return random.randint(1, 6)

    def get_score(self):
        return self.scores

    def roll_or_hold(self):
        action = ''
        while True:
            value = input("(R)oll or (H)old? ")
            if value.lower() == 'r':
                action = 'roll'
                break
            elif value.lower() == 'h':
                action = 'hold'
                break
        return action

    def play(self):

       """Start a game of Pig"""

       for player in cycle(self.players):

           print('Now rolling: {}'.format(player))

           action = 'roll'

           turn_points = 0

           while action == 'roll':

               value = self.roll()

               if value == 1:

                   print('{} rolled a 1 and lost {} points'.format(player, turn_points))

                   turn_points = 0

                   break

               turn_points += value

               print('{} rolled a {} and now has {} points for this turn'.format(

                   player, value, turn_points

               ))

               if self.scores[player] + turn_points >= 100:

                   self.scores[player] += turn_points

                   print('{} won the game with {} points!'.format(

                       player, self.scores[player]

                   ))

                   return

               action = self.roll_or_hold()

           self.scores[player] += turn_points

def main():

   """Launch a game of Pig"""

   game = Pig(*get_player_names())

   game.play()

if __name__ == '__main__':

   main()



