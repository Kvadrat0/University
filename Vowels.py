letters = input('Enter a string: ')
vowels = ['a', 'e', 'i', 'u', 'o']
i = 0
for letter in letters:
    if letter in vowels:
        i += 1
print(i, 'vowels in string')