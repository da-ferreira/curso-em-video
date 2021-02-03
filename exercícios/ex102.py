
def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número.
    :param numero: o número a ser calculado.
    :param show: Para mostrar o processo do cálculo do fatorial.
    :return: O valor do fatorial de um número x.
    """
    from time import sleep
    fact = 1

    if show:  # <- Se show for True.
        print('-=-' * 20)
        print(f'\nProcesso de fatorial do número {numero}:')
        sleep(1)
        for i in range(numero, 0, -1):
            if i != 1:
                print(f'{i} x ', end='')
                sleep(0.4)
            else:
                print(f'{i} = ', end='')
                sleep(0.4)

            fact *= i  # <- fatorial
        return fact  # <- Retornando o resultado do fatorial.

    else:  # <- Se for false, ou não tiver show.
        print('-=-' * 20)
        print(f'\nResultado do fatorial do número {numero}: ', end='')
        for j in range(numero, 0, -1):
            fact *= j
        return fact


num = int(input('\nDigite um número para saber seu fatorial: '))
while True:
    mostrar = int(input('[ 1 ] para ver o processo inteiro de cálculo'
                    '\n[ 2 ] para ver apenas o fatorial do número'
                    '\n[ 3 ] para ver a docstring da função.'
                    '\n>> Escolha: '))
    if mostrar not in range(1, 4):
        print('\nERRO! Escolha inválida, tente novamente.\n')
    else:
        if mostrar == 1:
            print(fatorial(num, show=True))
        elif mostrar == 2:
            print(fatorial(num))
        else:
            help(fatorial)
        break
