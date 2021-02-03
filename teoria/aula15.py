'''
-=-=-=-=- Comando break -=-=-=-=-
'''

soma = 0
while True:
    num = int(input('Informe um número: '))
    if num == 999:
     break
    soma += num
print(f'A soma vale {soma}.')