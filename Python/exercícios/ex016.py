import math
print('\n{}Transforma um número qualquer em porção inteira.{}'.format('\033[7;34m', '\033[m'))

num = float(input('\n\033[1;31mDigite um número:\033[m '))
print(f'O número \033[4;35m{num}\033[m tem a sua parte inteira \033[4;35m{math.trunc(num)}\033[m.')