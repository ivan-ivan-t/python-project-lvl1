import random

import prompt


def rules():
    print('What number is missing in the progression?\n')


def is_right(start, stop, step, length):
    for c in range(start, stop, step)[length - 1:length + 1]:
        return c


def answer(start, stop, step, length):
    print('Question: ', end='')
    for z in range(start, stop, step)[0:length - 1]:
        print(z, end=' ')
    print('..', end=' ')
    for x in range(start, stop, step)[length:10]:
        print(x, end=' ')
    return prompt.string('\nYour answer: ')


def logic_game(name):
    count = 3
    while count > 0:
        length = random.randint(1, 9)
        start = random.randint(1, 10)
        step = random.randint(1, 9)
        stop = 100
        user_answer = answer(start, stop, step, length)
        correct_answer = is_right(start, stop, step, length)
        if str(correct_answer) != user_answer:
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
