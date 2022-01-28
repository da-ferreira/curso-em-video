print('Números primos')

num = int(input('\nDigite um número inteiro para saber se ele é primo: '))
i = 0  # variável contadora

for contar in range(1, num + 1):
    if num % contar == 0:
        print('\033[1;32m', end='')  # green
        i += 1
    else:
        print('\033[1;31m', end='')  # red
    print('{} '.format(contar), end='')
print('\n\n\033[mO número {} foi divisível {} vezes'.format(num, i))
if i == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
