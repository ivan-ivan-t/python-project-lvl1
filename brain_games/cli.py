import prompt


def greeting():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    return name
