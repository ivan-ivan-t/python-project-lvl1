import random


DESCRIPTION = 'What is the result of the expression?'


def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def prepare_question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = '{a} {b} {c}'.format(a=num1, b=operator, c=num2)
    correct_answer = str(calculate(num1, operator, num2))
    return (correct_answer, question)
