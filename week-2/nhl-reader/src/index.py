from cli import Cli, CustomConsole, CustomPrompt


def main():
    prompt = CustomPrompt()
    console = CustomConsole()
    cli = Cli(prompt, console)

    console.print("Welcome to NHL statistics viewer.")
    console.print("Type 'help' to see the list of available commands.")

    while True:
        cli.execute()


if __name__ == "__main__":
    main()
