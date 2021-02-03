print('\n\033[4;33mConversor de medidas em metros\n\033[m')

metro = float(input('\033[1;31mDigite uma distância em metros: '))
centimetro = metro * 100
milimetro = metro * 1000

print(f'\nA medida de {metro}m corresponde a\033[m:')

print(f'\n\033[1;32m{metro / 1000}km')
print(f'{metro / 100}hm')
print(f'{metro / 10}dam')
print('{:.0f}dm'.format(metro * 10))
print('{:.0f}cm'.format(centimetro))
print('{:.0f}mm\033[m'.format(milimetro))
