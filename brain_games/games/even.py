import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no"'


def prepare_question_and_calculated():
    number = random.randint(1, 50)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return (correct_answer, question)
