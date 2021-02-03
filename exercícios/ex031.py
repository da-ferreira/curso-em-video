cor = {'l': '\033[m',
       'blue_underline': '\033[4;34m',
       'cyan_bold': '\033[1;36m'
       }

print('{}Custo da viagem.{}'.format(cor['blue_underline'], cor['l']))

viagem = float(input('\n{}Qual a distância da sua viagem em Km? '.format(cor['cyan_bold'])))

if viagem <= 200.0:
    custo = viagem * 0.50
else:
    custo = viagem * 0.45

#custo = viagem * 0.50 if viagem <= 200.0 else viagem * 0.45 #  <-- if simplificado/operador ternário

print('O custo da sua viagem é de {}R${:.2f}'.format(cor['blue_underline'], custo))
