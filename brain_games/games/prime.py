import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    else:
        return 'yes'


def prepare_question_and_calculated():
    number = random.randint(2, 100)
    question = str(number)
    correct_answer = is_prime(number)
    return (correct_answer, question)
