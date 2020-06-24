from brain_games import cli, even


def main():
    cli.greeting()
    even.rules()
    name = cli.welcome_user()
    even.logic_games(name)


if __name__ == '__main__':
    main()
