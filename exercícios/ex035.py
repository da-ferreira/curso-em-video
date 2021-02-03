print()
print('-=-' * 20)
print('Analisando se valores de retas podem formar um triângulo.')
print('-=-' * 20)

r1 = float(input('\nDigite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

#  Regra condição de existência de um triângulo.
if ((r2 - r3) < r1 < (r2 + r3)) and \
        ((r1 - r3) < r2 < (r1 + r3)) and \
        ((r1 - r2) < r3 < (r1 + r2)):
    print()
    print('-=-' * 14)
    print('Os comprimentos PODEM formar um triângulo.')
    print('-=-' * 14)
else:
    print()
    print('-=-' * 16)
    print('Os comprimentos NÃO podem formar um triângulo.')
    print('-=-' * 16)

# FIM DO MUNDO 1 DE PYTHON - CURSO EM VÍDEO(03/04/2020)
