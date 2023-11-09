n = int(input('Enter a number: '))
save = n
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(save,'! = ', factorial)