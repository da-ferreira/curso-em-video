"""
 -=-=- DICIONÁRIO -=-=-
"""

pessoas = {'nome': 'David', 'sexo': 'M', 'idade': 18}

print(pessoas['nome'])  # <- Mostrando o valor 'David' que pertence a chave 'nome'.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')


print(pessoas.keys())  # <- Mostra todas as chaves do dicionário (nome, sexo, idade).
print(pessoas.values())  # <- Mostra todos os valores do dicionário (David, M, 18).
print(pessoas.items())  # <- Mostra todos os itens do dicionário.


for k in pessoas.keys():  # <- Mostra todas as keys.
    print(k)

for v in pessoas.values():  # <- Mostra todos o valores.
    print(v)

for key, valor in pessoas.items():  # <- Mostra tudo.
    print(f'{key} = {valor}')

del pessoas['sexo']  # <- Apagando um item/elemento no dicionário.

pessoas['nome'] = 'Robson'  # <- alterando o valor de uma chave.

pessoas['peso'] = 55.3  # <- Adicionando um elemento ao final do dicionário.

print()

for key, valor in pessoas.items():
    print(f'{key} = {valor}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

brasil = list()

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)  # Adicionando dicionários dentro de uma lista.
brasil.append(estado2)

print(brasil)

print(brasil[0])  # Mostrando o 1ª elemento da lista (RJ)

print(brasil[0]['uf'])  # Mostrando o 1ª elemento da lista e sua chave 'uf'.

print(brasil[1]['sigla'])

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

estado = dict()
brasil = list()

for i in range(3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())  # <- Adicionando uma cópia de estado na lista brasil.

for estados in brasil:  # <- for para a lista
    for k, v in estados.items():  # <- k = key, v = value (chaves e valores)
        print(f'O campo {k} tem valor {v}.')

print()

for estados in brasil:  # <- Percorrendo somente os valores (nesse caso, os estado e suas siglas.)
    for v in estados.values():
        print(f'{v} - ', end='')
    print()
