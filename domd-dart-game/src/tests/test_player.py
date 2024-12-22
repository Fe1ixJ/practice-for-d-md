import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Test Player")

    def test_initial_attributes(self):
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.score, 0)

    def test_score_input(self):
        self.player.input_score(10)
        self.assertEqual(self.player.score, 10)

        self.player.input_score(5)
        self.assertEqual(self.player.score, 15)

    def test_invalid_score_input(self):
        with self.assertRaises(ValueError):
            self.player.input_score(-1)

if __name__ == '__main__':
    unittest.main()