import pydoc
class BowlingGame:
    """A class representing a game of bowling.

    Attributes:
        rolls (list): A list to store the number of pins knocked down in each roll.
    """

    def __init__(self):
        """Initialize a new instance of BowlingGame."""
        self.rolls = []

    def roll(self, pins):
        """Record a roll in the game.

        Args:
            pins (int): The number of pins knocked down in the roll.
        """
        self.rolls.append(pins)

    def score(self):
        """Calculate the total score of the game.

        Returns:
            int: The total score of the game.
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """Check if a roll is a strike.

        Args:
            rollIndex (int): The index of the roll to check.

        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """Check if a roll is a spare.

        Args:
            rollIndex (int): The index of the roll to check.

        Returns:
            bool: True if the roll is a spare, False otherwise.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        """Calculate the score for a frame with a strike.

        Args:
            rollIndex (int): The index of the roll where the strike occurred.

        Returns:
            int: The score for the frame with a strike.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        """Calculate the score for a frame with a spare.

        Args:
            rollIndex (int): The index of the roll where the spare occurred.

        Returns:
            int: The score for the frame with a spare.
        """
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """Calculate the score for a frame without a strike or spare.

        Args:
            rollIndex (int): The index of the first roll in the frame.

        Returns:
            int: The score for the frame without a strike or spare.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
documentation = pydoc.render_doc(BowlingGame)

# Write the documentation to an HTML file
with open("BowlingGame.html", "w") as f:
    f.write(documentation)