import random


RULES = 'Answer "yes" if number even otherwise answer "no"\n'


def question_and_correct_answer():
    number = random.randint(1, 50)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return (correct_answer, question)
