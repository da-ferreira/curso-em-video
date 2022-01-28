
brasileirao = (
    'Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
    'Atlético-PR', 'São Paulo', 'Internacional',
    'Corinthians', 'Fortaleza', 'Goiás', 'Bahia',
    'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',
    'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
)

print('\nTabela do Brasileirão 2019\n')
for i in range(len(brasileirao)):  # <- Mostrando a tabela inteira.
    print(f'{i+1 :2}ª  {brasileirao[i]}')
print('-=-' * 6)

print('\nOs 5 primeiros colocados são:\n')
for i in range(5):
    print(f'{i+1}ª {brasileirao[i]}')
print('-=-' * 6)

print('\nOs 4 últimos são:\n')
for i in range(16, 20):
    print(f'{i+1}ª {brasileirao[i]}')
print('-=-' * 6)

print('\nTimes em ordem alfabética:\n')
brasileirao_alfabetico = sorted(brasileirao)  # <- Colocando os times em ordem alfabética.
for i in range(len(brasileirao)):
    print(f'{brasileirao_alfabetico[i]}')
print('-=-' * 6)

print(f'\nA chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição.')
