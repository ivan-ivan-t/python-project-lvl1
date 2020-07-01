from brain_games import cli
from brain_games.games import calc


def main():
    cli.greeting()
    calc.rules()
    name = cli.welcome_user()
    calc.logic_game(name)


if __name__ == '__main__':
    main()
