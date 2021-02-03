print('TABUADA')

num = int(input('\nDigite um número para ver sua tabuada: '))

print()
print('-=-' * 4)
for contar in range(1, 11):
    print('{} x {:2} = {}'.format(num, contar, (num * contar)))
print('-=-' * 4)
