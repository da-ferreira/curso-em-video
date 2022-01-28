from random import randint
from time import sleep


def sorteia(lista):
    print('\nSorteando 5 valores para uma lista: ', end='')
    for i in range(5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
        sleep(0.5)
    print('PRONTO!')


def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []

sorteia(numeros)
soma_par(numeros)  # <- Mostrando o resultado da soma dos valores pares sorteados.
