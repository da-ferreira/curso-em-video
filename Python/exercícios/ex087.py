print('\nMATRIZ\n')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
dados = [[], []]  # <- Índice 0 para os números pares, 1 para soma da 3ª coluna.

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i}, {j}]: '))

        if matriz[i][j] % 2 == 0:
            dados[0].append(matriz[i][j])
        if j == 2:  # <- Ou seja, o número faz parte da 3ª coluna da matriz.
            dados[1].append(matriz[i][j])
print('~~' * 10)

for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j] :^6}', end='')
    print()
print('~~' * 10)

print(f'\nA soma dos valores pares é {sum(dados[0])}.')
print(f'A soma dos valores da terceira coluna é {sum(dados[1])}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
