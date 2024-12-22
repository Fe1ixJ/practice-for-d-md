import unittest
from game.scoring import Scoring

class TestScoring(unittest.TestCase):

    def setUp(self):
        self.scoring = Scoring()

    def test_calculate_score(self):
        self.assertEqual(self.scoring.calculate_score(10, 5), 15)
        self.assertEqual(self.scoring.calculate_score(0, 0), 0)
        self.assertEqual(self.scoring.calculate_score(-5, 5), 0)

    def test_display_score(self):
        self.assertEqual(self.scoring.display_score(15), "Score: 15")
        self.assertEqual(self.scoring.display_score(0), "Score: 0")

if __name__ == '__main__':
    unittest.main()