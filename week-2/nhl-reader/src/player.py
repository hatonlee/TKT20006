import requests


class Player:
    def __init__(self, player_data):
        self.name = player_data["name"]
        self.team = player_data["team"]
        self.nationality = player_data["nationality"]
        self.goals = player_data["goals"]
        self.assists = player_data["assists"]

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:<20} {self.team:>15} {self.goals:>3} + {self.assists:<3} = {self.points:<3}"


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError:
            return None

        players = [Player(player_data) for player_data in response]
        return players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_points_by_nationality(self, nationality):
        if not self.players:
            return None

        filtered_players = filter(lambda p: p.nationality == nationality, self.players)
        sorted_players = sorted(filtered_players, key=lambda p: p.points, reverse=True)
        return sorted_players

    def get_all_countries(self):
        return set(player.nationality for player in self.players)


def create_url(year):
    return f"https://studies.cs.helsinki.fi/nhlstats/{year}-{int(str(year)[2:]) + 1}/players"


def get_top_players(year, nationality):
    url = create_url(year)
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_points_by_nationality(nationality)
    return players

def get_countries(year):
    url = create_url(year)
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    countries = stats.get_all_countries()
    return countries