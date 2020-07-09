import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no"\n'


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    else:
        return 'yes'


def question_and_correct_answer():
    number = random.randint(2, 100)
    question = str(number)
    correct_answer = is_prime(number)
    return (correct_answer, question)
