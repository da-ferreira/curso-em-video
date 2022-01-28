print('-.-' * 6)
print(f'LOJA DO XURUPITA')
print('-.-' * 6)

total = produto_maior_1000 = i = preco_mais_barato = 0

while True:
    produto = str(input('\nNome do produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    i += 1  # Para validar o produto mais barato

    if i == 1 or preco < preco_mais_barato:
        nome_mais_barato = produto
        preco_mais_barato = preco  # Preço do produto mais barato

    total += preco
    if preco > 1000:
        produto_maior_1000 += 1

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('\n-==- FIM DA COMPRA -==-')
print(f'O valor total da compra foi R${total :2f}'
      f'\n{produto_maior_1000} produtos tiveram preço maior do que R$1000.00'
      f'\nO produto mais barato foi {nome_mais_barato} que custa R${preco_mais_barato :.2f}')
