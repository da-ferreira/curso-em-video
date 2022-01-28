cor = {'cyan_underline': '\033[4;36m',
       'l': '\033[m',
       'cyan_bold': '\033[1;36m',
       'green_bold': '\033[1;32m',
       'red_bold': '\033[1;31m'
       }

print('{}Radar eletrônico.{}'.format(cor['cyan_underline'], cor['l']))

velocidade = float(input('\n{}A que velocidade o carro está: km\h '.format(cor['cyan_bold'])))
#  Se o carro ultrapassar 80km\h ele será multado.
valor_multa = 7.0
if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7.0
    print('\nSeu veiculo ultrapassou 80km\h.\n{}Você foi multado!{}{}\nPague {:.2f}R$ para o DETRAN.'.
          format(cor['red_bold'], cor['l'], cor['cyan_bold'], multa))
else:
    print('\n{}O veiculo está numa velocidade adequada.\n{}:)'.format(cor['green_bold'], cor['cyan_bold']))
