import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def prepare_question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    question = '{a} {b}'.format(a=num1, b=num2)
    correct_answer = str(gcd(num1, num2))
    return (correct_answer, question)
