from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    nationality = "FIN"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_points_by_nationality(nationality)

    print("Players with nationality [{nationality}]:")
    print(f"{"Name":<30} {"Team":>20} {"Points":>15}")
    print("-" * (20 + 15 + 10 + 10 + 10 + 4 + 4))

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
