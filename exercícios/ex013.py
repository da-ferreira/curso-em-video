print('\n{}Reajuste salarial{}'.format('\033[7;30m', '\033[m'))

salario = float(input('\nDigite o valor do salário: {}R$'.format('\033[1;33m')))
calculo = (salario * 15) / 100
aumento = salario + calculo

print('\n{}O salário recebeu {}15% de aumento{} e esta valendo: {}R${:.2f}{}'.format('\033[m', '\033[1;33m',
                                                                                     '\033[m', '\033[1;33m',
                                                                                     aumento, '\033[m'))
