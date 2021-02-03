import random
cor = {
       'limpar': '\033[m',
       'verde_negrito': '\033[1;32m',
       'negativo': '\033[7;37m',
       'red_bold': '\033[1;31m'
       }

print('\n{}Sorteio de um aluno para apagar o quadro.{}'.format(cor['negativo'], cor['limpar']))

aluno1 = input('\n{}Primeiro aluno: '.format(cor['verde_negrito']))
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno:{} '.format(cor['limpar']))
lista = [
         aluno1,
         aluno2,
         aluno3,
         aluno4
         ]
escolhido = random.choice(lista)

print('\nParabéns {}{}{}, você foi escolhido para apagar o quadro.'.format(cor['red_bold'], escolhido, cor['limpar']))
