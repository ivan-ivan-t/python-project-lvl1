import random

import prompt


RULES = 'Answer "yes" if number even otherwise answer "no"\n'


def right_result(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question_and_correct_answer():
    number = random.randint(1, 50)
    question = ('Question: {}'.format(number))
    correct_answer = right_result(number)
    return (correct_answer, question)
