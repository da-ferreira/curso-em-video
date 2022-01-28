print('-=-' * 9 + '=')
print('CONVERSOR DE BASES NÚMERICAS')
print('-=-' * 9 + '=')

base = int(input('\nQue base de conversão você deseja usar?\n'
                 '\nDigite [ 1 ] para usar binário'
                 '\nDigite [ 2 ] para usar octal'
                 '\nDigite [ 3 ] para usar hexadecimal\n'))

if base == 1:
    print()
    print('-=-' * 3)
    print('BINÁRIO')
    print('-=-' * 3)

    num = int(input('\nDigite um número inteiro: '))

    print('O número {} em BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
    #  O '[:2]' inicia a a frase começando pelo 2° digito, ignorando 0 e 1.
elif base == 2:
    print()
    print('-=-' * 2)
    print('OCTAL')
    print('-=-' * 2)

    num = int(input('\nDigite um número inteiro: '))

    print('O número {} em OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print()
    print('-=-' * 4)
    print('HEXADECIMAL')
    print('-=-' * 4)

    num = int(input('\nDigite um número inteiro: '))

    print('O número {} em HEXADECIMAL é igual a {}'.format(num, hex(num).upper()[2:]))
else:
    print('O valor digitado não corresponde a nenhuma base de conversão!'
          '\nTente Novamente.')
