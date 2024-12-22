import unittest
from game.opponent import Opponent

class TestOpponent(unittest.TestCase):

    def setUp(self):
        self.opponent_easy = Opponent(level='easy')
        self.opponent_medium = Opponent(level='medium')
        self.opponent_hard = Opponent(level='hard')

    def test_generate_score_easy(self):
        score = self.opponent_easy.generate_score()
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 50)

    def test_generate_score_medium(self):
        score = self.opponent_medium.generate_score()
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_generate_score_hard(self):
        score = self.opponent_hard.generate_score()
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 150)

if __name__ == '__main__':
    unittest.main()