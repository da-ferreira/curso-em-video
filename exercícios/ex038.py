print('\n{}Comparando números.{}'.format('\033[7;30m', '\033[m'))

n1 = int(input('\n{}Digite o primeiro número: '.format('\033[1;36m')))
n2 = int(input('digite o segundo número:{} '.format('\033[m')))

if n1 > n2:
        print('\n{}O PRIMEIRO valor é o maior.'.format('\033[1;32m'))
elif n2 > n1:
    print('\n{}O SEGUNDO valor é maior.'.format('\033[1;32m'))
else:
    print('\n{}NÃO existe valor maior, os dois são IGUAIS'.format('\033[4;31m'))
