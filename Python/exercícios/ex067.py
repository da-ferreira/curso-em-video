print('-=- TABUADA -=-\n')

while True:
    num = int(input('Informe um número para ver sua tabuada: '))
    if num < 0:
        break
    print('~=' * 6)
    for i in range(1, 11):
        print(f'{num} x {i :2} = {num * i}')
    print('~=' * 6)
print('\nTABUADA ENCERRADA\nVolte sempre :)')
