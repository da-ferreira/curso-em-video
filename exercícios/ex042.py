print('\nAnalisando Triângulos.')

r1 = float(input('\nDigite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

#  Regra condição de existência de um triângulo.
if ((r2 - r3) < r1 < (r2 + r3)) and \
        ((r1 - r3) < r2 < (r1 + r3)) and \
        ((r1 - r2) < r3 < (r1 + r2)):

    if (r1 == r2) and (r1 == r3):
        print('\nOs comprimentos PODEM formar um triângulo.'
              '\nO triângulo formado será EQUILÁRETO, pois, todos seus lados são iguais.')

    elif (r1 != r2) and (r2 != r3) and (r3 != r1):
        """"((r1 != r2) and (r1 != r3)) and \
            ((r2 != r1) and (r2 != r3)) and \
            ((r3 != r1) and (r3 != r2)):"""
        print('\nOs comprimentos PODEM formar um triângulo.'
              '\nO triângulo formado será ESCALENO, pois, todos seus lados são diferentes.')

    else:
        print('\nOs comprimentos PODEM formar um triângulo.'
              '\nO triângulo formado será ISÓSCELES, pois, tem dois lados iguais.')
else:
    print('\nOs comprimentos NÃO PODEM formar um triângulo.')
