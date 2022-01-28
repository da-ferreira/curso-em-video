print('Progressão Aritmética v2')

termo = int(input('\nInforme o primeiro termo da P.A: '))
razao = int(input('Informe a razão da P.A: '))
i = 1

while i <= 10:
    print(termo, end=' → ')
    termo += razao
    i += 1
print('FIM')
