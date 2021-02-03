"""
  -=-=- CONTINUAÇÃO: LISTAS -=-=-
"""

teste = list()
teste.append('David')
teste.append(18)

galera = list()
galera.append(teste[:])  # <- Fazendo uma cópia da estrutura.

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])  # Idem

print(galera)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galera[1][0])  # <- Pegando o item 'Ana'
print(galera[3][0])  # <- Pegando o item 'Maria'

for i in galera:
    print(f'{i[0]} tem {i[1]} anos de idade.')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

galera = list()
dado = list()
maiores = menores = 0

for i in range(3):
    dado.append(input('\nNome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # <- Pegando uma cópia de 'dado' e colocando em galera.
    dado.clear()  # <- Limpando a lista.

for item in galera:
    if item[1] >= 21:  # <- Só quem for maior que 21 anos.
        print(f'{item[0]} é maior de idade.')
        maiores += 1
    else:
        print(f'{item[0]} é menor de idade.')
        menores += 1

print(f'Temos {maiores} maiores e {menores} menores de idade.')
