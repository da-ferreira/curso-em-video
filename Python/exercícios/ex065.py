print('Maior e menor valores | Média\n')

resposta = ''  # Resposta do usuário
media = i = 0  # i é a contagem dos números digitados
numeros = []  # Lista dos números

while resposta in 'Ss':
    num = int(input('Informe um número inteiro: '))
    media += num
    i += 1
    numeros += [num]
    resposta = str(input('Quer continuar informando valores? [Sim|Nao] ')).strip()[0]

print('\nA média entre os {} valores informados é igual a {:.2f}.'
      '\nO maior valor informado é {}.\nO menor valor informado é {}.'
      .format(i, (media / i), max(numeros), min(numeros)))
