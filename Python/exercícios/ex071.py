print('===' * 10)
print('{:^30}'.format('BANCO XURUPITA'))
print('===' * 10)

while True:
    valor = int(input('\nQuanto você quer sacar? R$'))
    print('-=-' * 10)

    if valor >= 50:  # Valores maiores que 50
        cinquenta = valor // 50
        print(f'Total de {cinquenta} cédulas de R$50')

    resto = valor % 50
    if resto != 0 and resto >= 20:
        vinte = resto // 20
        print(f'Total de {vinte} cédulas de R$20')

    resto = ((valor % 50) % 20)
    if resto != 0 and resto >= 10:
        dez = resto // 10
        print(f'Total de {dez} cédulas de R$10')

    resto = (((valor % 50) % 20) % 10)
    if resto != 0 and resto >= 1:
        um = resto // 1
        print(f'Total de {um} cédulas de R$1')
    break
print('-=-' * 10)
print('\nVolte sempre ao Banco Xurupita!\nTenha um bom dia :)')

'''
Só tem cédulas de R$ 50, 20, 10 e 1.
A lógica do programa é: Pegar o resto da divisão do valor retirado
e dividir por 20 em diante.
Se for um valor que dê para pegar só notas em 50,
ele faz a divisão truncada por 50 e pega o resultado.
'''

# FIM DO MUNDO 2 DE PYTHON - CURSO EM VÍDEO(07/05/2020)
