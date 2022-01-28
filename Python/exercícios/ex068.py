from random import randint
from time import sleep

print('=~' * 18, '')
print('COMPUTADOR: VAMOS JOGAR PAR OU ÍMPAR')
print('=~' * 18, '\n')

vitorias = soma = 0  # Quantas VEZES o usuário venceu e a SOMA dois valores.

while True:
    while True:  # Validando a escolha do jogador
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
        if escolha in 'PI':
            break
    jogador = int(input('Diga o número: '))
    pc = randint(0, 20)  # Escolha do computador
    soma = jogador + pc

    print('=*' * 17)
    print(f'Você jogou {jogador} e o computador {pc}')
    print(f'O total dá {soma}, então deu', 'PAR.' if soma % 2 == 0 else 'ÍMPAR.')
    print('=*' * 17)
    sleep(2)

    if ((escolha == 'P') and (soma % 2 == 0)) or \
            ((escolha == 'I') and (soma % 2 == 1)):  # Jogador vence se a soma der par ou de ímpar.
        print('¨¨¨' * 5)
        print('VOCÊ VENCEU!')
        print('¨¨¨' * 5)
        vitorias += 1

    elif ((escolha == 'P') and (soma % 2 != 0)) or \
            (escolha == 'I') and (soma % 2 != 1):  # Jogar perde porque a soma da diferente de sua escolha.
        print('¨¨¨' * 5)
        print('VOCÊ PERDEU!')
        print('¨¨¨' * 5)
        break  # Interrompendo a repetição

    print('COMPUTADOR: Vamos jogar novamente...')

print(f'\nGAME OVER! Você venceu {vitorias} vezes')
