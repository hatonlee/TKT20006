from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, count, criteria=SortBy.POINTS):
        if criteria == SortBy.GOALS:
            sorted_players = sorted(self._players, reverse=True, key=lambda player: player.goals)
            return sorted_players[:count]
        if criteria == SortBy.ASSISTS:
            sorted_players = sorted(self._players, reverse=True, key=lambda player: player.assists)
            return sorted_players[:count]
        else:
            sorted_players = sorted(self._players, reverse=True, key=lambda player: player.points)
            return sorted_players[:count]