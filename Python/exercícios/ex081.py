
numeros = list()

while True:
    numeros.append(int(input('\nInforme um número: ')))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=-' * 17)
numeros.sort(reverse=True)  # <- Deixando a lista em ordem decrescente.

print(f'Você informou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são {numeros}.')

if 5 in numeros:
    print('O valor 5 faz parte dessa lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
