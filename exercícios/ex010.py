print('\n\033[1;35mCoversor de moedas(Euro, dolar e libra)\033[m')

real = float(input('\n\033[1;31mQuantos de dinheiro você quer converter:R$\033[m'))
dolar = real / 4.80
euro = real / 5.35
libra_esterlina = real / 5.94

print(f'\nNa cotação atual, de 12 de março de 2020, com \033[1;33m{real}\033[mR$ você pode comprar:')
print('\n\033[1;33m{:.2f}\033[mUS$\n\033[1;33m{:.2f}\033[meur€\n\033[1;33m{:.2f}\033[mgbp£'
      .format(dolar, euro, libra_esterlina))
