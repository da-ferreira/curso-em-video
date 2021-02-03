cor = {
       'negative': '\033[7;30m',
       'cyan_bold': '\033[1;36m',
       'red_bold': '\033[1;31m',
       'l': '\033[m'
       }


print('{}Separador de digitos de um número.{}'.format(cor['negative'], cor['l']))

num = int(input('\n{}Digite um número de 0 a 9999: '.format(cor['cyan_bold'])))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('\nAnalisando o número {}...{}'.format(num, cor['l']))
print('\nUnidade: {}{}{}'.format(cor['red_bold'], unidade, cor['l']))
print('Dezena: {}{}{}'.format(cor['red_bold'], dezena, cor['l']))
print('Centena: {}{}{}'.format(cor['red_bold'], centena, cor['l']))
print('Milhar: {}{}'.format(cor['red_bold'], milhar))
