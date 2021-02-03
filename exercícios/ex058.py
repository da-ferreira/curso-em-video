from random import randint

print('JOGO DA ADIVINHAÇÃO\n')

computador = randint(0, 10)
tentativas = 1

print('-=-' * 23)
print('COMPUTADOR: Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 23)

usuario = int(input('\nEm que número eu pensei: '))

while usuario != computador:
    tentativas += 1
    if usuario < computador:
        print('\nCOMPUTADOR: Mais...')
    elif usuario > computador:
        print('\nCOMPUTADOR: Menos...')
    usuario = int(input('Tente Novamente: '))
print('\nParabens você acertou!\nSeu número de tentativas foi {}.'.format(tentativas))
