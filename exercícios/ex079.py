
valores = []

while True:
    valor = int(input('\nDigite um valor: '))
    if valor not in valores:
        print('Valor adicionado com sucesso!')
        valores.append(valor)
    else:
        print('VALOR DUPLICADO! Não vou adicionar...')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

valores.sort()  # <- Deixando a lista em ordem crescente.
print(f'\nVocê digitou os valores {valores}')
