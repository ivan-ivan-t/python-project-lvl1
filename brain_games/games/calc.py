import random

import prompt


RULES = 'What is the result of the expression?\n'


def right_result(num1, operand, num2):
    if operand == '+':
        return num1 + num2
    elif operand == '-':
        return num1 - num2
    elif operand == '*':
        return num1 * num2


def question_and_correct_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operand = random.choice(['+', '-', '*'])
    question = ('Question: {a} {b} {c}'
          .format(a=num1, b=operand, c=num2))
    correct_answer = str(right_result(num1, operand, num2))
    return (correct_answer, question)
