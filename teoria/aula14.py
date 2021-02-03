'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Estrutura de repetição com while
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim...')


n = 1
while n != 0:  # Condição de parada
    n = int(input('Digite um valor: '))
print('Valor aceito!')


r = 'S'
while r == 'S':  # Condição de parada
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim...')
'''

n = 1
par = impar = 0  # mesmo que separar os dois em duas linhas, porque as variáveis tem o mesmo valor.
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números impares e {} números pares.'.format(impar, par))
