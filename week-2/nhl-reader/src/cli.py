import sys
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from player import get_top_players, get_countries

class CustomPrompt(Prompt):
    prompt_suffix = "> "


class CustomConsole(Console):
    def print_help(self):
        self.print("Available commands:")
        self.print("list countries")
        self.print("list seasons")
        self.print("set country")
        self.print("set season")
        self.print("print")
        self.print("exit")

    def create_player_table(self, year, nationality):
        table = Table(title=f"Players from [{nationality}] in {year}",
                      show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan", width=20)
        table.add_column("Team", style="cyan", width=15)
        table.add_column("Goals", style="cyan", width=15)
        table.add_column("Assists", style="cyan", width=15)
        table.add_column("Points", style="cyan", width=15)

        return table

    def display_players(self, players, year, nationality):
        if not players:
            self.print(f"No players from [{nationality}] in {year}", style="bold red")
            return

        table = self.create_player_table(year, nationality)

        for player in players:
            table.add_row(player.name, player.team, str(player.goals),
                        str(player.assists), str(player.points))

        self.print(table)


class Cli:
    def __init__(self, prompt, console):
        self.prompt = prompt
        self.console = console
        self.year = None
        self.nationality = None
        self.players = []

    def get_command(self):
        command = self.prompt.ask()
        return command

    def execute(self):
        command = self.get_command()

        match command:
            case "help":
                self.console.print_help()

            case "list countries":
                if not self.year:
                    self.console.print("Select a season first.", style="bold yellow")
                    return
                countries = get_countries(self.year)
                countries_str = f"[{"/".join(countries)}]"
                self.console.print(f"Available countries: {countries_str}")

            case "list seasons":
                self.console.print("Available seasons: 2018-2025")

            case str() if command.startswith("set country "):
                self.nationality = command.split("set country ")[1]
                self.console.print(f"Selected country: {self.nationality}")

            case str() if command.startswith("set season "):
                year_str = command.split("set season ")[1]
                try:
                    new_year = int(year_str)
                    if 2018 <= new_year <= 2025:
                        self.year = new_year
                        self.console.print(f"Selected season updated: {self.year}")
                    else:
                        self.console.print(f"Not a valid year: '{year_str}'", style="bold red")
                except ValueError:
                    self.console.print(f"Not a valid year: '{year_str}'", style="bold red")

            case "print":
                if not self.year or not self.nationality:
                    self.console.print("Select the country and season first.", style="bold yellow")
                else:
                    self.players = get_top_players(self.year, self.nationality)
                    self.console.display_players(self.players, self.year, self.nationality)

            case "exit":
                sys.exit()

            case _:
                self.console.print("Invalid command. Type 'help' for a list of available commands.",
                                    style="bold red")
