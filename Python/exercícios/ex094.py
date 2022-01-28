
pessoas = []  # <- Lista para guardar todas as pessoas.
cadastro = {}  # <-  Dicionário que armazena cada pessoa.
soma_idade = 0

while True:
    cadastro['Nome'] = input('\nNome: ').title()

    sexo = input('Sexo: [M/F] ').strip().upper()[0]
    while sexo not in 'MF':
        print('Por favor, informe o sexo somente por M ou F.')
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    cadastro['Sexo'] = sexo

    cadastro['Idade'] = int(input('Idade: '))
    soma_idade += cadastro['Idade']

    pessoas.append(cadastro.copy())  # <- Colocando os dados na lista.

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        print('Por favor, informe usando apenas S(sim) ou N(não).')
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('-=-' * 19)
media = soma_idade / len(pessoas)  # <- Média de idade das pessoas.

print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media :5.2f}.')

print(f'- As mulheres cadastradas foram: ', end='')  # <- Listando as mulheres cadastradas.
for i in pessoas:
    if i['Sexo'] == 'F':
        print(f'[{i["Nome"]}]', end=' ')

print(f'\n- Lista das pessoas que estão acima da média: \n')  # <- Pessoas acima da média.
for j in pessoas:
    if j['Idade'] >= media:
        print('    ', end='')
        for key, valor in j.items():
            print(f'{key}: {valor}; ', end='')
        print()

print('\n<<< ENCERRADO >>>')
