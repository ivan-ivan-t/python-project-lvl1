from brain_games import cli

from brain_games.games import progression


def main():
    cli.greeting()
    progression.rules()
    name = cli.welcome_user()
    progression.logic_game(name)


if __name__ == '__main__':
    main()
