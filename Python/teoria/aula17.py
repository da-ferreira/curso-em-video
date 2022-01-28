'''
  -=-=- LISTAS -=-=-
'''


num = [2, 5, 9, 1]
num[2] = 3  # <- Mudando o elemento 2 para 3

num.append(7)  # <- Adicionando um valor ao final da lista.

num.sort()  # <- Colocando a lista em ordem CRESCENTE.
num.sort(reverse=True)  # <- Colocando a lista em ordem DECRESCENTE.

num.insert(2, 2)  # <- Na posição 2 inserindo o valor 2.

num.remove(2)  # <- Remove o primeiro elemento de valor 2.
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')

num.pop()  # <- Eliminando o último elemento da lista.
num.pop(2)  # <- Eliminando o elemento 2.

print(num)
print(f'Essa lista tem {len(num)} elementos.')  # <- LEN conta quantos elementos tem.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

valores = list()

for v in valores:
    print(f'{v}...', end='')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

for v in range(len(valores)):  # <- Outra forma de mostrar os valores.
    print(f'Na posição {v} encontrei {valores[v]}!')
print('FINAL DA LISTA..')


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


for i in range(5):  # <- Lendo valores e adicionando dentro das listas.
    valores.append(int(input('Digite o valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('FINAL DA LISTA..')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

a = [2, 3, 4, 7]

b = a
b[2] = 8  # <- Quando igualo uma lista a outra, ao adicionar valores a uma o python coloca nas duas.

b = a[:]  # <- b recebe todos os itens de a, b faz uma cópia de a. b não tem nenhuma ligação com a.
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
