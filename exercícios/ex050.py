print('SOMA DE PARES\n')

c = 0  # variável contadora
soma = 0  # variável acumuladora
for contar in range(1, 7):
    num = int(input('Digite o {}º número: '.format(contar)))
    if num % 2 == 0:
        soma += num
        c += 1
print('\nA soma dos {} números pares digitados é igual a {}.'.format(c, soma))

