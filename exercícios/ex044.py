print('{:=^40}'.format(' LOJAS XURUPITA '))  # O {:^40} é centralizado em 40 espaços

produto = float(input('\nPreço das compras: R$'))

condicao = float(input('FORMAS DE PAGAMENTO\n'
                       '\n[ 1 ] à vista com dinheiro/cheque.'  # 10% de desconto.
                       '\n[ 2 ] à vista no cartão.'  # 5% de desconto.
                       '\n[ 3 ] em até 2x no cartão.'  # Preço normal.
                       '\n[ 4 ] em 3x ou mais no cartão.\n'))  # 20% de juros.

if condicao == 1:
    print('\nSua compra de R${:.2f} recebeu 10% de desconto e vai custar R${:.2f}.'
          .format(produto, (produto * 0.9)))
elif condicao == 2:
    print('\nSua compra de R${:.2f} recebeu 5% de desconto e vai custar R${:.2f}.'
          .format(produto, (produto * 0.95)))
elif condicao == 3:
    print('\nSua compra será parcela em 2x de {:.2f} SEM JUROS.'.format(produto / 2))
    print('O valor da compra é R${:.2f}'.format(produto))
elif condicao == 4:
    juros = produto * 1.20
    parcela = int(input('Quantas parcelas? '))
    vezes = juros / parcela
    print('\nSua compra será parcelada em {}x de R${:.2f} COM JUROS.'
          '\nSua compra de R${:.2f} recebeu 20% de juros e vai custar R${:.2f}.\n'
          .format(parcela, vezes, produto, juros))
else:
    print('\nO valor digitado não corresponde a nenhuma condição de pagamento!')
