import random


RULES = 'Answer "yes" if number even otherwise answer "no"\n'


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question_and_correct_answer():
    number = random.randint(1, 50)
    question = str(number)
    correct_answer = is_even(number)
    return (correct_answer, question)
