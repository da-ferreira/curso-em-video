
numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('\nInforme um valor: ')))

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('~~' * 20)

print(f'\nA lista completa é {numeros}')
print(f'A lista com pares é {pares}')
print(f'A lista com ímpares é {impares}')
