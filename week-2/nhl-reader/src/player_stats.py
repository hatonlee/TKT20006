from player_reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_points_by_nationality(self, nationality):
        return sorted(filter(lambda p: p.nationality == nationality, self.players), key=Player.points, reverse=True)