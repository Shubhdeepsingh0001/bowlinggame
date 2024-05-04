# test_BowlingGame.py
import unittest
from BowlingGame import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """A test case for the BowlingGame class."""

    def setUp(self):
        """Set up the test fixture."""
        self.game = BowlingGame()

    def roll_many(self, pins, rolls):
        """Roll a certain number of times with a given number of pins knocked down.

        Args:
            pins (int): The number of pins knocked down in each roll.
            rolls (int): The number of rolls to perform.
        """
        for _ in range(rolls):
            self.game.roll(pins)

    def test_gutter_game(self):
        """Test calculating score for a gutter game (all rolls are 0)."""
        self.roll_many(0, 20)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        """Test calculating score for a game with all rolls knocking down one pin."""
        self.roll_many(1, 20)
        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        """Test calculating score for a game with one spare."""
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(0, 17)
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        """Test calculating score for a game with one strike."""
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0, 16)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        """Test calculating score for a perfect game (all strikes)."""
        self.roll_many(10, 12)
        self.assertEqual(self.game.score(), 300)

if __name__ == "__main__":
    unittest.main()
