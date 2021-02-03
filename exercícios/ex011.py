cor = {
       'limpar': '\033[m',
       'amarelo_negrito': '\033[1;33m',
       'vermelho_negrito': '\033[1;31m',
       'azul_sublinhado': '\033[4;34m'
       }

print('\n{}Cálculo da área de uma parede e litros de tinta necessário para pintá-la.{}'
      .format(cor['amarelo_negrito'], cor['limpar']))

largura = float(input('\n{}largura da parede em metros? '.format(cor['vermelho_negrito'])))
altura = float(input('Altura da parede em metros?{} '.format(cor['limpar'])))
area = largura * altura
tinta = area / 2

print('\nA área dessa parede é igual: {}{} m²{}.'.format(cor['azul_sublinhado'],
                                                         area, cor['limpar']))
print('Será necessário {}{:.2f} litros de tinta{} para pintá-la!'.format(cor['azul_sublinhado'],
                                                                         tinta, cor['limpar']))
s