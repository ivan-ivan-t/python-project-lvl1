import random


DESCRIPTION = 'What is the result of the expression?'


def right_result(num1, operators, num2):
    if operators == '+':
        return num1 + num2
    elif operators == '-':
        return num1 - num2
    elif operators == '*':
        return num1 * num2


def prepare_question_and_calculated():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operators = random.choice(['+', '-', '*'])
    question = '{a} {b} {c}'.format(a=num1, b=operators, c=num2)
    correct_answer = str(right_result(num1, operators, num2))
    return (correct_answer, question)
