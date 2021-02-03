print('SOMA DE ÍMPARES MÚLTIPLOS DE TRÊS')

soma = 0
i = 0
for contar in range(3, 501, 6):
        soma += contar
        i += 1
print('\nA soma de todos os {} números ímpares múltiplos de 3 entre 1 e 500 é: {}'.format(i, soma))
