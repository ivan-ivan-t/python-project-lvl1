from brain_games import cli

from brain_games.games import prime


def main():
    cli.greeting()
    prime.rules()
    name = cli.welcome_user()
    prime.logic_game(name)


if __name__ == '__main__':
    main()
