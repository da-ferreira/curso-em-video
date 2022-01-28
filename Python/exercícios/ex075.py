valores = pares = ()

for i in range(1, 5):
    num = int(input(f'Digite o {i}ª número: '))
    valores += (num,)
    if num % 2 == 0:
        pares += (num,)

print(f'\nVocê digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')  # Contando quantas vezes o 9 aparece.

print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição' if 3 in valores
else f'O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram {pares}')
