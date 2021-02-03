
pessoas, pesos = [], []

while True:
    pessoas.append([str(input('\nNome: ')).title()])  # Criando uma lista em pessoas.
    pessoas[-1].append(float(input('Peso: ')))  # <- Adicionando os pesos na lista acima.
    pesos.append(pessoas[:][-1][1])  # <- Adicionando apenas os pesos das pessoas.

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('~~' * 25)

print(f'\nAo todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {max(pesos)}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == max(pesos):
        print(f'[{i[0]}]', end=' ')

print(f'\nO menor peso foi de {min(pesos)}Kg. Peso de ', end='')
for j in pessoas:
    if j[1] == min(pesos):
        print(f'[{j[0]}]', end=' ')
print()
