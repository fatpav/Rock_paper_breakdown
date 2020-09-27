import unittest
from src.game import *
from src.player import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Paul", "paper")
        self.player2 = Player("Simon", "rock")

    def test_player_1_wins(self):
        self.assertEqual("Player 1 Wins!!!", compare_choices(self, self.player1.choice, self.player2.choice))

    def test_player_2_wins(self):
       player1 = Player("Paul", "rock")
       player2 = Player("Simon", "paper")
       self.assertEqual("Player 2 Wins!!!", compare_choices(self, player1.choice, player2.choice))

    def test_players_draw_game(self):
        player1 = Player("Paul", "paper")
        player2 = Player("Simon", "paper")
        self.assertEqual("It's a draw!!", compare_choices(self, player1.choice, player2.choice))
