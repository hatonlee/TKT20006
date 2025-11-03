import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)

    print("Players with nationality [FIN]:")
    print(f"{"Name":<30} {"Team":>20} {"Goals":>10} {"Assists":>10}")
    print("-" * (30 + 20 + 10 + 10 + 3))

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
