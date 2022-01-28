
valores = []
for i in range(5):
    valores.append(int(input(f'Informe valor da posição {i}: ')))

print('\nSeu valores são: ', end='')
for i in valores:
    print(f'{i}', end=' ')

print(f'\nO MAIOR valor é {max(valores)} que aparece nas posições: ', end='')
for i in range(len(valores)):
    if valores[i] is max(valores):
        print(f'{i}', end='; ')

print(f'\nO MENOR valor é {min(valores)} que aparece nas posições: ', end='')
for i in range(len(valores)):
    if valores[i] is min(valores):
        print(f'{i}', end='; ')
print()
