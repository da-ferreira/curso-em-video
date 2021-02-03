cor = {'red': '\033[1;31m',
       'yellow': '\033[1;33m',
       'l': '\033[m'}

print('{}Super Progressão Aritmética{}'.format(cor['red'], cor['l']))

termo = int(input('\n{}Informe o primeiro termo da P.A: '.format(cor['yellow'])))
razao = int(input('Informe a razão da P.A:{} '.format(cor['l'])))
i = 1  # variável contadora do primeiro while
mais_termo = 1
j = 1  # variável contadora do segundo while
contar = 0  # Contagem de termos

while i <= 10:
    print(cor['red'], termo, cor['l'], end=' → ')
    termo += razao
    i += 1
    contar += 1
print('PAUSADO')
while mais_termo != 0:
    mais_termo = int(input('\n{}Quantos termos mais você quer ver na P.A:{} '.format(cor['yellow'], cor['l'])))
    while j <= mais_termo:
        print(cor['red'], termo, cor['l'], end=' → ')
        termo += razao
        j += 1
        contar += 1
    print('PAUSADO' if mais_termo != 0 else '')
    j = 1
print('\n{}Progressão Aritmética finalizada com {} termos exibidos.'.format(cor['yellow'], contar))
