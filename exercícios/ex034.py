print('Aumento de salário.')

salario = float(input('\nQual é o valor do seu salário? R$'))

if salario > 1250.00:
    #  Se o salário for maior do que 1250R$ ele recebe um aumento de 10%.
    print('\nSeu salário de {:.2f}R$ recebeu um aumento de 10% e está valendo {:.2f}R$.'.format(salario,
                                                                                                (salario * 1.1)))
else:
    #  Se o salário for menor do que 1250R$ ele recebe um aumento de 15%.
    print('\nSeu salário de {:.2f}R$ recebeu um aumento de 15% e está valendo {:.2f}R$.'.format(salario,
                                                                                                (salario * 1.15)))
