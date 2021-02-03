nome = str(input('Qual é o seu nome? '))
if nome == 'David':
    print('Que nome lindo!')
elif nome == 'Rafael' or nome == 'Maria' or nome == 'Felipe':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Bianca xurupita Carlos':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

'''estrutura condicional aninhada
aninhada por que está em formato de ninho
'''