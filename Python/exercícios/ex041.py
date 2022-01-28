from datetime import date

print('Classificando atletas')

ano = int(input('\nEm que ano você nasceu? '))
idade = date.today().year - ano
print('\nO atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Você está na categoria MIRIM.')
elif (idade >= 10) and (idade <= 14):
    print('Você está na categoria INFANTIL.')
elif (idade >= 15) and (idade <= 19):
    print('Você está na categoria JUNIOR.')
elif (idade >= 20) and (idade <= 25):
    print('Você está na categoria SÊNIOR.')
elif idade > 25:
    print('Você está na categoria MASTER.')
