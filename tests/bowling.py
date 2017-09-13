import unittest
import random

from src.bowling import BowlingGame

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def roller(self, times, pins):
        for i in range(times):
            self.game.roll(pins)

    def test_rolls_all_zeros(self):
        self.roller(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_rolls_all_ones(self):
        self.roller(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_rolls_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roller(17, 0)
        self.assertEqual(self.game.score(), 16)

    def test_rolls_no_spares(self):
        self.roller(4, 0)
        self.game.roll(3)
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(2)
        self.roller(12, 0)
        self.assertEqual(self.game.score(), 15)

    def test_a_strike(self):
        self.roller(4, 0)
        self.game.roll(10)
        self.game.roll(2)
        self.game.roll(3)
        self.game.roll(4)
        self.roller(11, 0)
        self.assertEqual(self.game.score(), 24)

    def test_rolls_one_strike(self):
        self.roller(2, 0)
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.roller(14, 0)
        self.assertEqual(self.game.score(), 24)

    def test_all_strikes_except_last_frame(self):
        self.roller(9, 10)
        self.game.roll(3)
        self.game.roll(5)
        self.assertEqual(self.game.score(), 259)

    def test_final_strike(self):
        self.roller(18, 0)
        self.game.roll(10)
        self.game.roll(7)
        self.game.roll(2)
        self.assertEqual(self.game.score(), 19)

    def test_final_spare(self):
        self.roller(18, 0)
        self.game.roll(3)
        self.game.roll(7)
        self.game.roll(2)
        self.assertEqual(self.game.score(), 12)

    def test_perfect_game(self):
        self.roller(12, 10)
        self.assertEqual(self.game.score(), 300)

if __name__ == '__main__':
    unittest.main()
