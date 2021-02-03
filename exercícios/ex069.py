print('-=- CADASTRAMENTO DE PESSOAS -=-\n')

maioridade = homens = mulher_menor_20 = i = 0

while True:
    i += 1
    print('=-=' * 10)

    print(f'CADASTRO DA {i}ª PESSOA')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:  # Quantas pessoas que tem mais de 18 anos.
        maioridade += 1
    if sexo == 'M':  # Quantos homens.
        homens += 1
    if sexo == 'F' and idade < 20:  # Quantas mulheres com menos de 20 anos.
        mulher_menor_20 += 1

    continuar = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar cadastrando? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('\n== FIM DO CADASTRO ==')
print(f'\nTotal de pessoas com mais de 18 anos: {maioridade}'
      f'\nTotal de homens cadastrados: {homens}'
      f'\nTotal de mulheres com menos de 20 anos: {mulher_menor_20}')
