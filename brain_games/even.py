from random import randint

import prompt


def rules():
    print('Answer "yes" if number even otherwise answer "no"\n')


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def answer(number):
    print('Question: {}'.format(number))
    return prompt.string('Your answer: ')


def logic_games(name):
    count = 3
    while count > 0:
        number = randint(1, 50)
        correct_num = is_even(number)
        user_answer = answer(number)
        if correct_num != user_answer:
            print(
                """
'{a}' is wrong answer ;(. Correct answer was '{b}'.
Let's try again, {c}!
                """.format(a=user_answer, b=correct_num, c=name))
            break
        else:
            print('Correct!')
        count -= 1
    if count == 0:
        print('Congratulations, {}!'.format(name))
