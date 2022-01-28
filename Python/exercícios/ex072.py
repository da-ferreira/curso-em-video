
numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    num = -1
    while num not in range(21):  # Se o número não estiver no intervalo de 0 e 20.
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[num]}.\n')

    continuar = ' '
    while continuar not in 'SN':  # Enquanto a resposta não estiver em 'S' ou 'N'.
        continuar = input('Quer continuar digitando números? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
