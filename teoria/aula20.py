"""
 -=-=- FUNÇÕES/MÉTODOS -=-=-
"""


def mensagem(texto):
    print('-' * 30)
    print(f'{texto :^30}')
    print('-' * 30)


mensagem('BEM VINDO')

nome = input('Qual seu nome? ')

mensagem(f'PRAZER, {nome.title()}')


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def soma(a, b):
    print(f'\nA = {a}, B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)

soma(a=8, b=10)  # <- Explicitando os parametros
soma(b=9, a=15)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def contador(*num):  # <- Recebe um número ilimitado de parametros, armazenando-os em uma tupla.
    tamanho = len(num)
    print(f'Você informou os valores {num} e são {tamanho} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def dobra_valor(lista):  # <- Dobrando o valor de cada elemento da lista.
    for posicao in range(len(lista)):
        lista[posicao] *= 2


valores = [6, 3, 9, 1, 0, 2]
dobra_valor(valores)
print(valores)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def soma_valor(*valores):  # Desempacotamento
    resultado = 0
    for num in valores:
        resultado += num
    print(f'Somando os valores {valores} temos {resultado}')


soma_valor(5, 2)
soma_valor(2, 9, 4)
soma_valor(1, 2, 3, 4, 5, 6, 10)
