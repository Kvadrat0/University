import random


def not_change(choice):
    return choice[random.randrange(len(choice))]


def change(choice):

    first = random.randrange(len(choice))
    for i in range(len(choice)):
        if i != first and choice[i] != 'w':
             host_choice = i
    for i in range(len(choice)):
        if i != first and i != host_choice:
            return choice[i]


def honty_mall():
    attempts = int(input('Сколько раз вы хотите провести тест?'))
    doors = ['l', 'l', 'w']
    count = 0
    for i in range(attempts):
        result = not_change(doors)
        if result == 'w':
            count += 1
    print('Шанс выиграть, если не менять выбор:', count/attempts)
    count = 0
    for i in range(attempts):
        result = change(doors)
        if result == 'w':
            count += 1
    print('Шанс выиграть, если поменять выбор:', count/attempts)


def birthday():
    amount = int(input('Количество человек в группе:'))
    chance = 1
    for i in range(amount):
        chance *= (1 - i/365)
    percent = round((1 - chance) * 100, 2)
    print(f'Шанс совпадения дней рождения у двух любых человек в группе равна {percent}%')
