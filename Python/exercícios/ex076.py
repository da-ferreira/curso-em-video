listagem = (
    'Pão', 0.50, 'Caderno', 12.50,
    'Dolly', 7.00, 'Cigarro', 3.50,
    'Lápis', 1.50, 'Estojo', 3.80,
    'Mochila', 80.00, 'Compasso', 9.98,
    'Livro', 35.85
)

print('-=-' * 15)
print(f'{"LISTA DE COMPRAS" :^46}')  # <- Nome formatado entre 46 espaços.
print('-=-' * 15)

for item in listagem:
    if type(item) is str:  # Se o elemento da tupla for tipo str ele printa.
        print(f'{item :.<30}', end='')
    else:  # Se não for, que no caso só resta os preços, ele printa os preços.
        print(f' R$ {item :5.2f}')
print('-=-' * 15)
