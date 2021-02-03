cor = {'l': '\033[m',
       'magenta_bold': '\033[1;35m',
       'cyan_bold': '\033[1;36m',
       'red_bold': '\033[1;31m'
       }

print('{}Par ou ímpar{}'.format(cor['magenta_bold'], cor['l']))

numero = int(input('\n{}Digite um número para saber se é par ou ímpar: '.format(cor['cyan_bold'])))

if numero % 2 == 0:
    print('\nO número {}{} é PAR.'.format(cor['red_bold'], numero))
else:
    print('\nO número {}{} é ÍMPAR.'.format(cor['red_bold'], numero))
