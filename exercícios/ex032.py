from datetime import date

cor = {'l': '\033[m',
       'magenta_underline': '\033[4;35m',
       'cyan_bold': '\033[1;36m',
       'red_bold': '\033[1;31m',
       'green_bold': '\033[1;32m'
       }

print('{}Ano bissexto.{}'.format(cor['magenta_underline'], cor['l']))

ano = int(input('\n{}Digite um ano para saber se ele é bissexto.'
                '\nColoque 0 para analisar o ano atual: '.format(cor['cyan_bold'])))

if ano == 0:
    ano = date.today().year  # Para saber o ano atual da máquina.
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    # Primeiro ele faz p(ano % 4) AND q(ano % 100) e o resultado isso faz OR com (ano % 400)
    print('\nO ano de {} {}é bissexto.'.format(ano, cor['green_bold']))
else:
    print('\nO ano de {} {}não é bissexto.'.format(ano, cor['red_bold']))
