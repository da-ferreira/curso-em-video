'''
-=-=- TUPLAS -=-=-

** TUPLAS SÃO IMUTÁVEIS **

lanche = () TUPLA
lanche = {} lista
lanche = [] dicionário
'''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # <-- TUPLA

# lanche[1] = 'Refrigerante'  # <--- Comando errado
print(lanche[1])  # <-- Mostrando todos os elementos dentro da tupla.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

for comida in lanche:  # <-- Fazendo uma repetição com todos os elementos.
    print(f'Eu vou comer {comida}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print(len(lanche))  # <-- Quantos elementos tem na tupla

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')  # <-- Mostrando os elementos na posição de cont.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

for posicao, comida in enumerate(lanche):  # <--- Mostra a posição do elemento na tupla.
    print(f'Eu vou comer {comida} na posição {posicao}')

print('To com buxim chei!')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print(sorted(lanche))  # <-- SORTED deixa a tupla organizada

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

numeros = (2, 5, 4)
mais_numeros = (5, 8, 1, 2)
soma = numeros + mais_numeros  # <-- Usando o mais+ elas se juntam.

print(soma.count(10))  # <-- Quantas vezes aparece o número 5.
print(soma)
print(soma.index(8))  # <-- Mostra a posição do x.
print(soma.index(2, 1))  # <-- Mostra a posição do 2 a partir da posição 1

pessoa = ('David', 17, 'M', 50.29)  # <-- As tuplas em python aceitam vários tipos de elementos.
print(pessoa)
del pessoa  # <-- Apagando uma variável
