cor = {
    'l': '\033[m',
    'blue_bold': '\033[1;34m',
    'cyan_bold': '\033[1;36m',
    'red_underline': '\033[4;31m',
    'red_bold': '\033[1;31m',
    'green_bold': '\033[1;32m',
    'yellow_bold': '\033[1;33m'
    }

print('\n{}ÍNDICE DE MASSA CORPORAL{}'.format(cor['blue_bold'], cor['l']))

peso = float(input('\n{}Qual seu peso em kg? '.format(cor['cyan_bold'])))
altura = float(input('Qual sua altura em metros? '))
imc = peso / (altura**2)

print('\nSeu índice de massa corporal é {:.1f}'.format(imc))

if imc < 18.5:
    print('{}Você está abaixo do peso.'.format(cor['yellow_bold']))
elif (imc >= 18.5) and (imc < 25):
    print("{}Você está no peso ideal.".format(cor['green_bold']))
elif (imc >= 25) and (imc < 30):
    print('{}Você está em sobrepeso.'.format(cor['yellow_bold']))

elif (imc >= 30) and (imc < 40):
    print('{}Você está com obesidade.'.format(cor['red_bold']))
elif imc >= 40:
    print('{}Você está com obesidade morbida.'.format(cor['red_underline']))
