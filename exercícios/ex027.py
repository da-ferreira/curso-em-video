cor = {
       'l': '\033[m',
       'red_underline': '\033[4;31m',
       'cyan_bold': '\033[1;36m',
       'white_bold': '\033[1;30m'
       }

print('{}Primeiro último nome de uma pessoa.{}'.format(cor['red_underline'], cor['l']))

nome = str(input('\n{}Digite seu nome completo:{} '.format(cor['cyan_bold'], cor['l']))).title().strip().split()
primeiro = nome[0]
ultimo = nome[-1]

print('\nPrazer em te conhecer, {}!\nPrimeiro nome: {}.\nÚltimo nome: {}.'.format(' '.join(nome), primeiro, ultimo))
