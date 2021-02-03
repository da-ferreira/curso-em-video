print('Validação de Dados')

sexo = input('\nQual seu sexo? [M|F]: ').upper().strip()[0]  # Somente a primeira letra é usada

while sexo not in 'MF':  # Enquanto o sexo NÃO ESTIVER em 'MF'.
    sexo = input('Sexo inválido. Por favor, informe seu sexo: [M|F] ').upper().strip()[0]  # Idem linha 3
print('\nSexo {} registrado com sucesso.'.format(sexo))
