from math import factorial
print('FATORIAL DE UM NÚMERO.\n')

num = int(input('Digite um número para saber seu fatorial: '))

fatorial = num

print('\n{}! = '.format(num), end='')
while fatorial > 0:
    print('{}'.format(fatorial), end='')
    print(' x ' if fatorial > 1 else ' = ', end='')  # Só mostrará x se o fatorial for maior que 1.
    fatorial -= 1
print('{}'.format(factorial(num)))
