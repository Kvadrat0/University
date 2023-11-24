import random

pc_guess = random.randint(0, 100)
attempts = 0

print('Компьютер загадал число!')

while True:
    guess = int(input('Введите число: '))
    if guess < pc_guess:
        print('Ваше число меньше загаданного!')
        attempts += 1
    elif guess > pc_guess:
        print('Ваше число больше загаданного!')
        attempts += 1
    else:
        print(f'Поздравляем! Вы угадали загаданное число за {attempts} попыток.')
        break
        