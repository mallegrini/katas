import unittest
from src.fizzbuzz import FizzBuzzer, Checker

class FizzBuzzerTest(unittest.TestCase):

	def setUp(self):
		self.m = FizzBuzzer((Checker(3, 'Fizz'), Checker(5, 'Buzz'), Checker(7, 'Bang')))

	def test_one_two(self):
		assert self.m.say(1) == "1"
		assert self.m.say(2) == "2"

	def test_fizz(self):
		assert self.m.say(3) == "Fizz"
		assert self.m.say(9) == "Fizz"

	def test_buzz(self):
		assert self.m.say(5) == "Buzz"
		assert self.m.say(10) == "Buzz"

	def test_fizzbuzz(self):
		assert self.m.say(15) == "FizzBuzz"
		assert self.m.say(30) == "FizzBuzz"

	def test_buzz(self):
		assert self.m.say(21) == "FizzBang"
		assert self.m.say(35) == "BuzzBang"
		assert self.m.say(21*5) == 'FizzBuzzBang'
