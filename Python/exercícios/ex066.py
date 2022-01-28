print('Tratando valores v2\n')

soma = i = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    i += 1
    soma += num
print(f'\nA soma dos {i} valores é igual a {soma}!')
