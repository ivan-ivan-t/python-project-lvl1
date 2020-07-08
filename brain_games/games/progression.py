import random

import prompt



RULES = 'What number is missing in the progression?\n'


def right_result(start, stop, step, length):
    for c in range(start, stop, step)[length - 1:length + 1]:
        return c

def progression(start, stop, step, length):
    print('Question: ', end='')
    for z in range(start, stop, step)[0:length - 1]:
        print(z, end=' ')
    print('..', end=' ')
    for x in range(start, stop, step)[length:10]:
        print(x, end=' ')

def question_and_correct_answer():
    length = random.randint(1, 9)
    start = random.randint(1, 10)
    step = random.randint(1, 9)
    stop = 100
    question = (progression(start, stop, step, length))
    correct_answer = str(right_result(start, stop, step, length))
    return (correct_answer, question)
