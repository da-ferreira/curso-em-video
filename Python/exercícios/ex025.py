cor = {
       'l': '\033[m',
       'green_underline': '\033[4;32m',
       'cyan_bold': '\033[1;36m'
       }

print('\n{}Verificando se uma pessoa tem SILVA no nome.{}'.format(cor['green_underline'], cor['l']))

nome = str(input('\n{}Digite seu nome completo: '.format(cor['cyan_bold']))).lower().strip().split()
# O split separou cada nome em uma contagem, assim analisou um por um e viu se tinha ou não silva.
silva = 'silva' in nome

print('\nEsse nome tem "silva"? \nAnalisando...{}'.format(cor['l']))
print('{}{}'.format(cor['green_underline'], silva))