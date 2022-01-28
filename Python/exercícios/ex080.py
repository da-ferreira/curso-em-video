
valores = list()

for i in range(1, 6):
    num = int(input(f'\nDigite o {i}ª valor: '))
    if i == 1 or num >= valores[-1]:  # Maior valor
        valores.append(num)
        print('Adicionado ao final da lista...')

    if num < valores[0] and i > 1:  # Menor valor
        valores.insert(0, num)
        print('Adicionado na posição 0 da lista...')

    elif i > 1 and num < valores[-1]:  # Valor médio
        for j in range(len(valores)):
            if num <= valores[j]:
                valores.insert(j, num)
                print(f'Adicionado na posição {j} da lista')
                break

print('-=-' * 18)

print(f'Os valores digitados em ordem foram {valores}')
