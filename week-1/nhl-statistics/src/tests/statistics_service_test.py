import unittest
from statistics_service import StatisticsService
from statistics_service import SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_correct_player(self):
        stats_player = self.stats.search("Semenko")
        test_player = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(str(stats_player), str(test_player))

    def test_search_returns_no_players(self):
        player = self.stats.search("Crosby")
        self.assertIs(player, None)

    def test_team_returns_correct_players(self):
        stats_players = self.stats.team("EDM")
        test_players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]

        stats_players = [str(player) for player in stats_players]
        test_players = [str(player) for player in test_players]

        self.assertEqual(stats_players, test_players)

    def test_top_returns_correct_players_by_points(self):
        stats_players = self.stats.top(3)
        test_players = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]

        stats_players = [str(player) for player in stats_players]
        test_players = [str(player) for player in test_players]

        print(stats_players)
        print(test_players)

        self.assertEqual(stats_players, test_players)

    def test_top_returns_correct_players_by_goals(self):
        stats_players = self.stats.top(3, SortBy.GOALS)
        test_players = [
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53)
        ]

        stats_players = [str(player) for player in stats_players]
        test_players = [str(player) for player in test_players]

        print(stats_players)
        print(test_players)

        self.assertEqual(stats_players, test_players)

    def test_top_returns_correct_players_by_assists(self):
        stats_players = self.stats.top(3, SortBy.ASSISTS)
        test_players = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Yzerman", "DET", 42, 56),
            Player("Lemieux", "PIT", 45, 54)
        ]

        stats_players = [str(player) for player in stats_players]
        test_players = [str(player) for player in test_players]

        print(stats_players)
        print(test_players)

        self.assertEqual(stats_players, test_players)