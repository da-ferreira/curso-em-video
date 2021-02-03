print('\n\033[1;31;40mCálculo de média de duas notas\033[m')

nota1 = float(input('\n\033[35mPrimeira nota: '))
nota2 = float(input('Segunda nota\033[m: '))
media = (nota1 + nota2) / 2

print('\nSua média é: \033[4;31m{:.1f}\033[m'.format(media))
