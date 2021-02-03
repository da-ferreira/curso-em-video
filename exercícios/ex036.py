cor = {'l': '\033[m',
       'red_bold': '\033[1;31m',
       'yellow_bold': '\033[1;33m',
       'grey_bold': '\033[1;36m',
       'green_bold': '\033[1;32m'}

print('\n{}APROVANDO EMPRÉSTIMO{}'.format(cor['yellow_bold'], cor['l']))

casa = float(input('\n{}Qual o valor da casa? R$'.format(cor['grey_bold'])))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Quantos anos de financiamento?{} '.format(cor['l'])))

mensalidade = casa / (anos * 12)

if mensalidade <= (salario * 0.30):  # 30% do salário.
    #  Se o valor da mensalidade for menor do que 30% do salario.
    print('{}Seu empréstimo foi aprovado com sucesso!{}'.format(cor['green_bold'], cor['l'], ))
    print('{}Durante {} anos você pagará uma prestação mensal de R${:.2f}.'.format(cor['grey_bold'],
                                                                                   anos, mensalidade))
else:
    print('{}Você não pode financiar esta casa!{}\n{}O valor da mensalidade seria de R${:.2f}'
          '\nSinto Muito.'.format(cor['red_bold'], cor['l'],
                                  cor['grey_bold'], mensalidade))
