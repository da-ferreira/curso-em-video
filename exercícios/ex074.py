from random import sample

numeros = tuple(sample(range(10), 5))  # Usando a função sample e gerando 5 números no intervalo de 0 a 10.

print(f'\nOs valores sorteados foram: {numeros}')
print(f'O maior valor sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')
