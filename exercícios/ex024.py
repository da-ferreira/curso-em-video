cor = {
       'l': '\033[m',
       'blue_bold': '\033[1;34m',
       'yellow_bold': '\033[1;33m',
       'cyan_bold': '\033[1;36m'
       }

print('{}Verificando se uma cidade começa com o nome "santo".{}'.format(cor['blue_bold'], cor['l']))

cidade = str(input('\n{}Digite o nome de uma cidade: '.format(cor['cyan_bold']))).lower().strip().split()
nome = 'santo' in cidade[0]
print('\nEssa cidade começa com nome o "santo"? \nAnalisando...{}\n{}{}'.format(cor['l'], cor['yellow_bold'], nome))
