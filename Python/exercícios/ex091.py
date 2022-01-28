
from random import randint
from time import sleep

ranking = dict()  # Dicionário para colocá-los em ordem.
jogadores = [[], [], [], []]  # Lista para guardar os jogadores

input('-=-=- JOGOS DE DADOS -=-=-')  # <- Dando início ao jogo de dados.
print('\nValores Sorteados: ')

for i in range(4):
    jogadores[i].append(randint(1, 6))  # <- Gerando um valor no dado.
    jogadores[i].append(f'jogador{i+1}')  # <- Jogador que gerou esse valor.

for i in range(4):
    print(f'    O {jogadores[i][1]} tirou {jogadores[i][0]}.')
    sleep(1)

jogadores.sort(reverse=True)  # <- Ranking

for i in range(4):
    ranking[jogadores[i][1]] = jogadores[i][0]  # O '[1]' é o nome, o '[0]' é o valor tirado.

print('Ranking:')

i = 1
for k, v in ranking.items():
    print(f'    {i}ª lugar: {k} com {v}')
    sleep(1)
    i += 1
