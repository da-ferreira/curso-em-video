print('\nDetector de Palíndromo')

frase = input('\nDigite uma frase/palavra para saber se ela é um palíndromo: ').lower()

frase2 = frase.strip().split()
palindromo = ''.join(frase2)
inverso = ''.join(frase2)[::-1]  # Começa a frase pela última letra.

if palindromo == inverso:
    print('\nO inverso de {} é {}.'.format(''.join(frase2).upper(), inverso.upper()))
    print('{}é um PALÍNDROMO.'.format('\033[1;32m', ))
else:
    print('\nO inverso de {} é {}.'.format(''.join(frase2).upper(), inverso.upper()))
    print('{}NÃO é um PALÍNDROMO.'.format('\033[1;31m'))
