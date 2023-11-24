import re


def open_file(file):
    text = open(file, encoding='utf-8').read().lower()
    word_pattern = r'[а-яё\-]+'
    words = re.findall(word_pattern, text)
    return words


def read_file(file):
    all_words = open_file(file)
    unique_words = []
    for word in all_words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


def save_file(file, unique):
    count = open(file, 'w', encoding='utf-8')
    count.write(f'Всего уникальных слов: {str(len(unique))}\n')
    count.write(f'---------------------\n')
    for i in range(len(unique)):
        count.write(f'{sorted(unique)[i]}\n')
    count.close()