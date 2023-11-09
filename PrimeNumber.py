prime = int(input('Enter a number: '))
for i in range(2, prime):
    if prime % i == 0:
        print(prime, 'is not a prime number!')
        break
    if i == prime - 1:
        print(prime, 'is a prime number!')