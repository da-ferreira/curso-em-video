print('Tratando Valores\n')

condicao = int(input('Digite um número inteiro: '))
soma = i = 0  # i é contagem.

while condicao != 999:
    print('Número inválido!')
    soma += condicao
    i += 1
    condicao = int(input('Digite um número inteiro: '))

print('\nNúmero válido!\nForam digitados {} números.'
      '\nA soma desses números é igual a {}.'.format(i, soma))
