from math import hypot

cor = {
       'limpar': '\033[m',
       'yellow_negrito': '\033[1;33m',
       'negativo': '\033[7;31m'
       }

print('\n{}Comprimento da hipotenusa de um triângulo retângulo.{}'.format(cor['negativo'], cor['limpar']))

c_oposto = float(input('\n{}Comprimento do cateto oposto: '.format(cor['yellow_negrito'])))
c_adjacente = float(input('Comprimento do cateto adjacente:{} '.format(cor['limpar'])))
hipotenusa = hypot(c_oposto, c_adjacente)

print('O comprimento da hipotenusa é igual a {}{:.2f}'.format(cor['yellow_negrito'], hipotenusa))
