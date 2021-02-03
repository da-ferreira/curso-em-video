from random import sample
from time import sleep

print()
print('-=-' * 5, end=' ')
print('PALPITES PARA A MEGA SENA ', end='')
print('-=-' * 5, end=' ')

jogos = int(input('\n\nQuantos jogos você quer que eu sorteie? '))

print(f'\n=-=-=-= SORTEANDO {jogos} JOGOS =-=-=-=')

for i in range(jogos):
    palpite = list(sample(range(1, 61), 6))
    palpite.sort()
    print(f'Jogo {i+1}: {palpite}' if jogos < 10 else f'Jogo {i+1 :2}: {palpite}', flush=False)
    sleep(1)
print('=-=-=-=-= < BOA SORTE! > =-=-=-=-=')
