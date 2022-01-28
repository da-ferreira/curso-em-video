
boletim = list()

while True:
    boletim.append([input('\nNome: ').title()])  # <- Criando uma lista dentro de boletim
    boletim[-1].append([float(input('1ª nota: '))])  # <- Criando uma lista dentro da lista criada acima.
    boletim[-1][-1].append(float(input('2ª nota: ')))  # <- Adicionando a segunda nota na lista criada acima.

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('~~' * 14)
print()

print(f'No. Nome      Média ')
print('-=-' * 8)
for i in range(len(boletim)):
    print(f'{i :<3} {boletim[i][0] :<10} {(sum(boletim[i][1]) / 2) :.1f}', end='')  # <- Mostrando o boletim.
    print()
print('-=-' * 8)

while True:
    nota = int(input('\nMostrar notas de qual aluno? (-1 para finalizar): '))
    if nota == -1:
        break
    if nota not in range(len(boletim)) and nota != -1:  # Tratando erros.
        print('ENTRADA INVÁLIDA!\nPor favor, tente novamente.')
    else:
        print(f'As notas de {boletim[nota][0]} são {boletim[nota][1]}')  # <- Mostrando o nome e a nota do aluno.
    print('~~~' * 12)

print('FINALIZANDO...\n<<< VOLTE SEMPRE! >>>')
