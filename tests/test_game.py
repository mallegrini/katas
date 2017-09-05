import unittest

from src import game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = game.RockPaperScissorsGame()

    def test_rock_beats_scissors(self):
        assert self.game.beats("rock", "scissors") == True

    def test_scissors_does_not_beat_rock(self):
        assert self.game.beats("scissors", "rock") == False

    def test_rock_does_not_beat_rock(self):
        assert self.game.beats("rock", "rock") == False

    def test_scissors_beats_papers(self):
        assert self.game.beats("scissors", "paper") == True

    def test_paper_beats_rock(self):
        assert self.game.beats("paper", "rock") == True

    def test_paper_does_not_beat_scissors(self):
        assert self.game.beats("paper", "scissors") == False

    def test_lizard_beats_scissors(self):
        assert self.game.beats("lizard", "scissors") == True