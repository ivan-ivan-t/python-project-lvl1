import random

import prompt


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no"\n'


def right_result(number):
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    else:
        return 'yes'


def question_and_correct_answer():
    number = random.randint(2, 100)
    question = 'Question: {}'.format(number)
    correct_answer = right_result(number)
    return (correct_answer, question)
