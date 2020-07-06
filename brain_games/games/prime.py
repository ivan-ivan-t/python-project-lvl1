import random

import prompt


def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no"\n')


def is_right(number):
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    else:
        return 'yes'


def answer(number):
    print('Question: {}'.format(number))
    return prompt.string('Your answer: ')


def logic_game(name):
    count = 3
    while count > 0:
        number = random.randint(2, 100)
        user_answer = answer(number)
        correct_answer = is_right(number)
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
