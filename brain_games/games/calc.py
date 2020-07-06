import random

import prompt


def rules():
    print('What is the result of the expression?\n')


def is_right(num1, operand, num2):
    if operand == '+':
        return num1 + num2
    elif operand == '-':
        return num1 - num2
    elif operand == '*':
        return num1 * num2


def answer(num1, operand, num2):
    print('Question: {a} {b} {c}'
          .format(a=num1, b=operand, c=num2))
    return prompt.string('Your answer: ')


def logic_game(name):
    count = 3
    while count > 0:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operand = random.choice(['+', '-', '*'])
        user_answer = answer(num1, operand, num2)
        correct_answer = is_right(num1, operand, num2)
        if str(correct_answer) != user_answer:
            print(
                """
'{a}' is wrong answer ;(. Correct answer was '{b}'.
Let's try again, {c}!
                """.format(a=user_answer, b=correct_answer, c=name))
            break
        else:
            print('Correct!')
        count -= 1
    if count == 0:
        print('Congratulations, {}!'.format(name))
