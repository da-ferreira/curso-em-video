print('Progressão Aritmética')

termo = int(input('\nInforme o primeiro termo da P.A: '))
razao = int(input('Informe a razão da P.A: '))
print()

for contar in range(1, 11,):
    print(termo, end=' ')
    termo += razao  # variável acumuladora
