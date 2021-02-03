print('\nMAIOR E MENOR PESO\n')

lista = []  # Lista vazia

for contar in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(contar)))
    lista += [peso]
print('\nO maior peso informado acima é {}Kg.'
      '\nO menor peso informado acima é {}Kg.'.format(max(lista), min(lista)))
