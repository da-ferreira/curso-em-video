from time import sleep
'''
Laço/iteração = uma estrutura de repetição.



for contar in range(1, 7):  # contar é uma variável
    print(contar)
print('FIM..')



for contar in range(6, 0, -1):  # o -1 é o modo como ela vai contar, nesse casso é de 6 a 0 tirando 1.
    print(contar)
print('FIM..')


for contar in range(80, -10, -2):  # Pulando de dois em dois.
    print(contar)
print('FIM..')


n = int(input('Digite um número: '))
for contar in range(n, 0-1, -1):  # Contagem regressiva de um número digitado até 0.
    sleep(0.5)
    print(contar)

print('boom..')


i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for contar in range(i, f+1, p):  # Lendo variáveis e jogando-as no for in range 
    print(contar)
print('fim..')

'''

s = 0
for contar in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
