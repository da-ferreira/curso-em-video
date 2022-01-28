
valores = [[], []]

for i in range(1, 8):
    num = int(input(f'Informe o {i}ª número: '))
    if num % 2 == 0:
        valores[0].append(num)  # <- Se o número for par.
    else:
        valores[1].append(num)  # <- Se o número for ímpar.

valores[0].sort()
valores[1].sort()

print(f'\nOs valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
