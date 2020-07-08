import prompt


def logic_game(game):
    print('Welcome to the Brain Games!')
    print(game.RULES)
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    count = 3
    while count > 0:
        correct_answer, question = game.question_and_correct_answer()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(
                """
'{a}' is wrong answer ;(. Correct answer was '{b}'.
Let's try again, {c}!
                """.format(a=user_answer, b=correct_answer, c=name))
            break
        else:
            print('Correct!')
        count -= 1
    if count == 0:
        print('Congratulations, {}!'.format(name))
