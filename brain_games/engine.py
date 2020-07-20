import prompt


def play(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {}!\n'.format(name))
    counter = 3
    while counter > 0:
        correct_answer, question = game.prepare_question_and_answer()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(
                """'{a}' is wrong answer ;(. Correct answer was '{b}'."""
                .format(a=user_answer, b=correct_answer))
            print("""Lets's try agane, {}!""".format(name))
            return
        print('Correct!')
        counter -= 1
    print('Congratulations, {}!'.format(name))
