print('\n\033[1;36mDobro, triplo e raiz quadrada de um número\033[m')

num = int(input('\n\033[1;31mDigite um número:\033[m '))
dobro = num * 2
triplo = num * 3
raiz = float(num) ** 0.5

print(f'\nO dobro de {num} é \033[1;31m{dobro}\033[m.\nO triplo de {num} é \033[1;31m{triplo}\033[m.')
print('A raiz quadrada de {} é \033[1;33m{:.2f}\033[m.'.format(num, raiz))
