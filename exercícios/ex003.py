cor = {
       'limpar': '\033[m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'negrito': '\033[1m',
       'amarelo_negrito': '\033[1;33m',
       'vermelho': '\033[31m'
       }

print('\n{}Soma de dois números{}'.format(cor['amarelo_negrito'], cor['limpar'] ))

n1 = int(input('\n{}Digite um número: '.format(cor['vermelho'])))
n2 = int(input('Digite outro número: {}'.format(cor['limpar'])))
soma = n1 + n2
print('A soma entre \033[1;33m{} \033[me \033[1;33m{} \033[mé igual a {}{}{}!'
      .format(n1, n2, cor['amarelo_negrito'], soma, cor['limpar']))
