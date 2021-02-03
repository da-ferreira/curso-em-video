cor = {
       'l': '\033[m',
       'cyan_bold': '\033[1;36m',
       'red_underline': '\033[4;31m',
       'green_bold': '\033[1;32m'
       }

from random import sample
print('\n{}Ordem de apresentação de trabalho dos alunos.{}'.format(cor['red_underline'], cor['l']))

aluno1 = input('\n{}Digite o nome do primeiro aluno: '.format(cor['cyan_bold']))
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno:{} '.format(cor['l']))

lista = [
         aluno1,
         aluno2,
         aluno3,
         aluno4
         ]
ordem = sample(lista, 4)  # o 4 representa quantos itens tem na lista. se colocar 3 apenas o indicado sera usado.

print('\n{}A ordem de apresentação dos trabalhos é a seguinte:{} \n{}{}'.format(cor['cyan_bold'], cor['l'],
                                                                                cor['cyan_bold'], ordem))
