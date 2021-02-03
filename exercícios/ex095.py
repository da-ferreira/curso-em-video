
jogadores = []  # <- Todos os jogadores.
cadastro = {}  # <- Cadastro de cada jogador.
gols = []  # <- Contagem de gols de cada jogador em cada partida.

while True:
    cadastro['Nome'] = input('\nNome do jogador: ').title().strip()
    partidas = int(input(f'Quantas partidas {cadastro["Nome"]} jogou: '))

    for i in range(partidas):
        gols.append(int(input(f'    •Quantos gols na {i+1}ª partida: ')))
    cadastro['Gols'] = gols.copy()
    cadastro['Total'] = sum(gols)

    jogadores.append(cadastro.copy())

    cadastro.clear(), gols.clear()  # <- Limpando.

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('-=-' * 18)

print(f"{'No.' :<2} {'Nome' :<14} {'Gols' :<8} {'Total' :>15}")
print('~~' * 22)

for i in range(len(jogadores)):
    print(f'{i :<3} {jogadores[i]["Nome"] :<12} {str(jogadores[i]["Gols"]) :<20}'
          f' {jogadores[i]["Total"] :<2}', end='')
    print()

print('~~' * 22)

while True:
    dados = int(input('\nMostrar dados de qual jogador? (999 para finalizar) '))
    if dados == 999:
        print('ENCERRANDO...')
        break
    elif dados not in range(len(jogadores)):  # Tratando erros.
        print(f'ERRO! Não existe jogador com numeração {dados}. Tente novamente')
    else:
        print(f'-=- LEVANTAMENTO DO JOGADOR {jogadores[dados]["Nome"]}:')
        for i in range(len(jogadores[dados]['Gols'])):
            print(f'    *No {i+1}ª jogo fez {jogadores[dados]["Gols"][i]} gols.')
    print('-=-' * 20)
print('\n<< VOLTE SEMPRE >>')
