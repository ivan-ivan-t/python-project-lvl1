import prompt


def logic_game(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {}!\n'.format(name))
    count = 3
    while count > 0:
        correct_answer, question = game.prepare_question_and_calculated()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(
                """
'{a}' is wrong answer ;(. Correct answer was '{b}'.
Let's try again, {c}!
                """.format(a=user_answer, b=correct_answer, c=name))
            return
        print('Correct!')
        count -= 1
    print('Congratulations, {}!'.format(name))
