print('\n{}Aluguel de carros{}'.format('\033[7;32m', '\033[m'))
#O carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('\n{}Quantos dias o carro foi alugado? '.format('\033[1;36m')))
km = float(input('Quantos Km rodados?{} '.format('\033[m')))
aluguel = (60 * dias) + (km * 0.15)

print('\n{}O total a pagar é de{} {}R${:.2f}'.format('\033[1;36m', '\033[m', '\033[1;33m', aluguel))
