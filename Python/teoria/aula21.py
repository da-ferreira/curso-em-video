"""
-=-=- CONTINUAÇÃO: FUNÇÕES -=-=-
"""


def contador(i, f, p):  # <- Função com docstring.
    """
     -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por David Ferreira. 08/06/2020
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


# contador(0, 100, 10)
help(contador)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def somar(a=0, b=0, c=0):  # <- Parâmetro opcional. Se o c não for informado ele vale 0.
    """
    -> Faz a soma de 3 valores e mostra o resultado na tela.
    :param a: para o primeiro valor
    :param b: para o segundo valor
    :param c: para o terceiro valor
    :return: sem retorno
    Função criada por David Ferreira, 08/06/2020.
    """
    soma = a + b + c
    print(f'A soma vale {soma}')


somar(3, 2, 5)
somar(8, 4)
somar()
help(somar)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def teste():
    x = 8  # <- a variável x tem um escopo local, pois foi declarada na função. Ela é uma variável local.
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {8}')


# Programa principal
n = 2  # <- A variável n tem um escopo global, funciona em todo o programa. Ela é uma variável global.
print(f'No programa principal, n vale {n}')
teste()

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def funcao(n):
    global n1  # <- Usando a variável a como global
    n1 = 4  # <- Essa variável não afeta a variável que está fora da função.
    n2 = 5
    n3 = 15
    print(f'N1 dentro vale {n1}')
    print(f'N2 dentro vale {n2}')
    print(f'N3 dentro vale {n3}')


n1 = 2
funcao(n1)
print(f'N1 fora vale {n1}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s  # <- Retorna o valor de s para alguma variável fora da função.


resposta = somar2(3, 2, 5)  # <- Recebendo o valor de s e jogando na variável.

r1 = somar2(3, 2, 5)  # <- Passando o resultado da função para uma variável.
r2 = somar2(2, 2)  # <- Idem linha 84
r3 = somar2(6)  # <- Idem

print(f'Os resultados foram {r1}, {r2} e {r3}.')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Parte prática da aula: Fazendo exercícios.


def fatorial(num=1):  # <- Valor opcional 1
    fact = 1  # <- Variável local.
    for i in range(num, 0, -1):
        fact *= i
    return fact


numero = int(input('Digite um número para saber seu fatorial: '))  # <- Variável global.
print(f'O fatorial de {numero} é igual a {fatorial(numero)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'\nOs resultados são {f1}, {f2} e {f3}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def par(num=0):  # <- Valor opcional 0.
    if num % 2 == 0:  # <- Se um número é par ou não.
        return True
    else:
        return False


number = int(input('\nDigite um número para saber se ele é par: '))

if par(number):
    print('É par!')
else:
    print('Não é par!')
