import random

import prompt


def rules():
    print('Find the greatest common divisor of given numbers.\n')


def is_right(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def answer(num1, num2):
    print('Question: {a} {b}'
          .format(a=num1, b=num2))
    return prompt.string('Your answer: ')


def logic_game(name):
    count = 3
    while count > 0:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        user_answer = answer(num1, num2)
        correct_answer = is_right(num1, num2)
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
