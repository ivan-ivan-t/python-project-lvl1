import random


RULES = 'What number is missing in the progression?\n'


def make_progression(start, step, lenght):
    counter = 0
    result = []
    next_number = start
    while counter < lenght:
        result.append(str(next_number))
        next_number += step
        counter += 1
    return result


def question_and_correct_answer():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    size = 10
    progression = make_progression(start, step, size)
    index = random.randint(0, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'
    question = ' '.join(progression)
    return (correct_answer, question)
