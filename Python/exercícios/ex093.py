
print('\n  -=-=- CADASTRO DE UM JOGADOR -=-=- \n')

jogador = {}  # <- Dados do jogador
gols = []  # <- Gols do jogador em cada partida jogada.

jogador['Nome'] = input('Nome do jogador: ').title()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))

for i in range(partidas):
    gols.append(int(input(f'    Quantos gols na {i+1}ª partida? ')))
jogador['Gols'] = gols.copy()
jogador['Total'] = sum(gols)
print('-=-' * 15)

print('DADOS:\n')
for key, valor in jogador.items():
    print(f'{key}: {valor}')
print('-=-' * 15, '\n')

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.\n')
for i in range(len(gols)):
    print(f'    => Na {i+1}ª partida, fez {gols[i]} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
