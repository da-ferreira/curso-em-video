import math
cor = {
       'limpar': '\033[m',
       'negativo': '\033[7;33m',
       'azul_negrito': '\033[1;34m'
       }

print('\n{}Conversor de um ângulo para seno, cosseno e tangente.{}'.format(cor['negativo'], cor['limpar']))

angulo = float(input('\n{}Digite o ângulo que você deseja:{} '.format(cor['azul_negrito'], cor['limpar'])))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print('\nO ângulo de {}° tem o valor de seno, cosseno e tangente igual a:'
      '\nSeno: {:.2f}'
      '\nCosseno: {:.2f}'
      '\nTangente: {:.2f}'.format(angulo, seno, cosseno, tangente))
