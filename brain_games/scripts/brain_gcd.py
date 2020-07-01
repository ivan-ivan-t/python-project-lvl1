from brain_games import cli
from brain_games.games import gcd


def main():
    cli.greeting()
    gcd.rules()
    name = cli.welcome_user()
    gcd.logic_game(name)


if __name__ == '__main__':
    main()
