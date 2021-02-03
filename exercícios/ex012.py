print('\n\033[1;35mDesconto do valor de um produto.\033[m')

preco = float(input('\n\033[1;36mQual o preço do produto? R$\033[m'))
soma = (preco * 5) / 100
desconto = preco - soma

print('\nO produto recebeu {}5%{} de desconto e esta valendo {}R${:.2f}{}!'.format('\033[1;31m', '\033[m',
                                                                                   '\033[1;31m', desconto,
                                                                                   '\033[m'))
