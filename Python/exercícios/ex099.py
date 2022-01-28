from time import sleep


def maior_valor(*valores):  # <- Recebe vários parametros e desempacota-os.
    maior = quantidade = 0
    print('\nAnalisando o(s) valor(es) ', end='')
    for i in valores:
        print(f'[{i}]', end=' ')
        quantidade += 1
        sleep(0.5)
    print(f'\nAo todo foram informados {quantidade} valores.')
    for j in range(len(valores)):
        if j == 1:
            maior = valores[j]
        else:
            if valores[j] > maior:
                maior = valores[j]
    print(f'O maior valor informado foi {maior}.')
    print('~~~' * 18)


maior_valor(1, 2, 3, 15, 3)
maior_valor(2, 3, 17, 5, 9, 15, 3, 10, 12)
maior_valor(6)
maior_valor(0)
maior_valor()
