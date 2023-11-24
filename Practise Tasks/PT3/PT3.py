import random
import wordop as wo
import record as rec


def letter_change(word, mask, turn):
    reserve = word
    for i in range(reserve.count(turn)):
        mask = mask[:reserve.find(turn)] + turn + mask[reserve.find(turn) + 1:]
        reserve = reserve.replace(turn, '*', 1)
    return mask


def difficulty():
    answer = input('Выберите уровень сложности!\n 1 - лёгкий (6 жизней)\n 2 - средний (4 жизни)\n 3 - сложный (2 жизни)\n 4 - экстремальный (1 жизнь)')
    while True:
        if answer == '1':
            return 6
        elif answer == '2':
            return 4
        elif answer == '3':
            return 2
        elif answer == '4':
            return 1
        else:
            answer = input('1 - лёгкий (6 жизней)\n 2 - средний (4 жизни)\n 3 - сложный (2 жизни)\n 4 - экстремальный (1 жизнь)')


def start_game(record):
    word = word_list.pop(random.randrange(len(word_list)))
    mask = '■' * len(word)
    lives = difficulty()
    #alphabet = [АБВГДЕЁЖЗИЙКЛМНОПРСТУФЦЧШЩЪЫЬЭЮЯ]

    while True:
        if lives == 0:
            print('У вас закончились жизни! Вы умерли! :\'(\nНеотгаданное слово было', word, '\nВы всего угадали:', record, 'слов.')
            break
        print(mask, f'🍔x{lives}')
        #print(word) #чит, который показывает слово
        if mask == word:
            record += 1
            print('Поздравляю! Вы победили!\nВы всего угадали', record, 'слов.')
            break

        turn = input("Назовите букву или всё слово целиком:").upper()

        while True:
            if len(turn) == 1 and turn not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФЦЧШЩЪЫЬЭЮЯ':
                turn = input("Назовите букву или всё слово целиком:").upper()
            else:
                break

        if len(turn) == 1 and turn in word:
            mask = letter_change(word, mask, turn)
        elif len(turn) == 1:
            print('Неправильная буква! Минус жизнь!')
            lives -= 1
        elif len(turn) == len(word) and turn == word:
            mask = word
        elif len(turn) == len(word) and turn != word:
            print('Неверное слово! Вы проиграли! :(\nНеотгаданное слово было:', word, '\nВы всего угадали', record, 'слов.')
            break
        else:
            print('Ошибка ввода: ожидалась буква или слово целиком!')
    if len(word_list) == 0:
        print('Все слова закончились! Спасибо за игру!')
    else:
        answer = input('Игра окончена! Хотите сыграть ещё?\n 1 - да, 2 - нет.')
        while True:
            if answer == '1':
                start_game(record)
                break
            elif answer == '2':
                print('Спасибо за игру!\nВсего вы угадали', record, 'слов')
                rec.write_record(record)
                break
            else:
                answer = input('1 - да, 2 - нет.')


word_list = wo.get_words()

record = 0
start_game(record)