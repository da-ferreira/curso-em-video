from time import sleep
print('Menu de Opções')

decisor = 0  # Tomada de decisão do programa

n1 = int(input('\nPrimeiro número: '))
n2 = int(input('Segundo número: '))

while decisor != 1:  # Enquanto o decisor não for 1 o programa fica em loop.
    menu = int(input('\n[ 1 ] somar'
                     '\n[ 2 ] multiplicar'
                     '\n[ 3 ] saber o maior número'
                     '\n[ 4 ] digitar novos números'
                     '\n[ 5 ] sair do programa'
                     '\n->>> Escolha o que pretende fazer: '))
    if menu == 1:
        print('\nA soma entre {} e {} é {}.'.format(n1, n2, (n1 + n2)))
    elif menu == 2:
        print('\no resultado de {} x {} é {}.'.format(n1, n2, (n1 * n2)))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\nEntre {} e {} o maior é {}.'.format(n1, n2, maior))
    elif menu == 4:
        print('\nInforme os números novamente.')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif menu == 5:
        print('Finalizando...')
        decisor = 1
    else:
        print('\nEntrada Inválida. Tente Novamente!')
    print('=-=' * 10)
    sleep(2)
print('\nPrograma finalizado. Obrigado por usar :)')
