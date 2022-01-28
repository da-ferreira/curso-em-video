print('~~' * 11)
print('SEQUÊNCIA DE FIBONACCI')
print('~~' * 11)

num = int(input('\nDigite o número de termos: '))
t1 = 0  # 1ª termo
t2 = 1  # 2ª termo
i = 3  # Contadora
print('-=-' * (num * 2))
print('{} → {}'.format(t1, t2), end='')

while i <= num:
    t3 = t1 + t2  # 3ª termo
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    i += 1
print(' → FIM')
print('-=-' * (num * 2))
'''
A lógica do programa é atualizar os dois primeiros termos para os valores anteriores.
Ou seja, o termo 1(t1) passa a ser o termo 2(t2), e o termo2(t2) passa a ser o termo 3(t3). 
'''