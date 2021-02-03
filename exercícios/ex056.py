print('ANALISADOR DE PESSOAS\n')

media = 0  # Média de idade do grupo
velho = 0  # Idade do homem mais velho
nome_velho = ''  # Nome do homem mais velho
mulher = 0  # Quantas mulheres tem menos que 20 anos.

for p in range(1, 5):
    print('--- {}ª PESSOA ---'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if (idade > velho) and (sexo == 'M'):
        velho = idade
        nome_velho = nome
    if (sexo == 'F') and (idade < 20):
        mulher += 1

print('\nA media de idade do grupo é de {} anos.'
      '\nO homem mais velho do grupo tem {} anos e se chama {}.'
      '\nNo grupo tem {} mulheres com menos de 20 anos.'
      .format((media / 4), velho, (nome_velho.capitalize()), mulher))
