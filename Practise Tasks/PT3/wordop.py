def get_words(path=r'C:\Users\mrleo\PycharmProjects\Informatika\Practise Tasks\PT3\words.txt'):
    text = open(path, encoding='utf8')
    text_list = text.read().upper().split(', ')
    text.close()
    return text_list