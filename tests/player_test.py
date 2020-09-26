import unittest

from src.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_has_choice(self):
        player_1 = Player("Paul", "Scissors")
        self.assertEqual("Scissors", player_1.choice)


    def test_player_name(self):
        player_1 = Player("Paul", "Scissors")
        self.assertEqual("Paul", player_1.name)

    