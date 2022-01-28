"""nome = str(input('Qual é seu nome? '))
if nome == 'David':
    print('Que nome lindo você tem! :)')
print('Bom dia, {}'.format(nome))"""

n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('\nDigite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:.1f}.'.format(media))
if media >= 6.0:
    print('Sua média foi boa, PARABÉNS MLKT!')
else:
    print('Ruim demais doido...')
