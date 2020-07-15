import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, round(num/2)):
        if num % i == 0:
            return False
    else:
        return True


def prepare_question_and_calculated():
    num = random.randint(1, 100)
    question = str(num)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return (correct_answer, question)
