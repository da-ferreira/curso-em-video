from random import randint
from time import sleep  # O metodo sleep faz o computador esperar por alguns segundos.

cor = {
    'l': '\033[m',
    'magenta_underline': '\033[4;35m',
    'green_bold': '\033[1;32m',
    'red_bold': '\033[1;31m',
    'cyan_bold': '\033[1;36m',
    'green_underline': '\033[4;32m',
    'red_underline': '\033[4;31m'
    }

print('\n{}JOGO DA ADIVINHAÇÃO{}\n'.format(cor['magenta_underline'], cor['l']))

computador = randint(0, 5)

print('{}{}{}'.format(cor['green_bold'], ('-=-' * 20), cor['l']))
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}'.format(cor['red_bold'], cor['l']))
#    Computador pensa em um número.
print('{}{}{}'.format(cor['green_bold'], ('-=-' * 20), cor['l']))

usuario = int(input('\n{}Que número eu pensei: '.format(cor['cyan_bold'])))  # jogador tenta advinhar

if usuario == computador:
    print('{}processando...{}'.format(cor['cyan_bold'], cor['l']))
    sleep(2)
    print('{}PARABÉNS, você acertou!\n:){}'.format(cor['green_bold'], cor['l']))
else:
    print('{}processando...{}'.format(cor['cyan_bold'], cor['l']))
    sleep(2)
    print('\n{}Você errou!\n:({}\n{}Eu pensei no número {} e não no {}.'.format(cor['red_bold'], cor['l'],
                                                                                cor['cyan_bold'],
                                                                                computador, usuario))
