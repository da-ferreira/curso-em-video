cor = {
       'red_underline': '\033[4;31m',
       'cyan_bold': '\033[1;36m',
       }

print('{}Maior e menor valores.'.format(cor['red_underline']))

num1 = int(input('\n{}Digite o primeiro número: '.format(cor['cyan_bold'])))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

lista = [
    num1,
    num2,
    num3
    ]

print('\nO menor valor digitado é {}.\nO maior valor digitado é {}'.format((min(lista)), max(lista)))
# O MAX antes da lista signigica pegar o maior valor dentro dela. O min pega o menor valor.


""" Outra forma de fazer
# Verificando quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Verificando quem é o maior

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('\nO menor valor  digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))"""
