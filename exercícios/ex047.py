from time import sleep

print('CONTAGEM DE PARES\n')

for contar in range(2, 51, 2):
    sleep(0.2)
    print(contar, end=' ')  # O end não termina a linha. Entre as aspas pode colocar qualquer coisa.
