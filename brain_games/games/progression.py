import random


DESCRIPTION = 'What number is missing in the progression?'


def prepare_question_and_answer():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    size = 10
    counter = 0
    progression = []
    while counter < size:
        progression.append(str(start + counter * step))
        counter += 1
    index = random.randint(0, size)
    correct_answer = str(start + index * step)
    progression[index] = '..'
    question = ' '.join(progression)
    return (correct_answer, question)
