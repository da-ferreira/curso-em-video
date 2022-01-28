cor = {
       'l': '\033[m',
       'red_underline': '\033[4;31m',
       'red_bold': '\033[1;31m',
       'cyan_bold': '\033[1;36m',
       'cyan_underline': '\033[4;36m'
       }

print('{}Analisador de um texto.{}'.format(cor['red_underline'], cor['l']))

nome = str(input('\n{}Digite seu nome completo: '.format(cor['cyan_bold']))).strip()
# o STRIP na última parte elimina os espaços inúteis.

minusculo = (nome.lower().strip())
maiuscula = (nome.upper().strip())
separar = nome.split()
letras_primeiro = len(separar[0])
# separei depois contei só a primeira parte.

letras_total = (len(nome) - nome.count(' '))
""" A função COUNT('x') conta quantos x tem no nome. 
    Acima usei primeiro o LEN para contagem e subtrai os espaços usando o COUNT."""

#letras_primeiro = nome.find(' ')
""" FIND indica o começa de um caractere.
    Nesse caso usei o (espaço) para achar o fim do primeiro nome e fazer a contagem."""

print('\n{}Analisando seu nome...{}'.format(cor['cyan_underline'], cor['l']))

print('\n{}Seu nome com letras minúsculas é: {}{}{}.'.format(cor['cyan_bold'], cor['red_bold'],
                                                             minusculo, cor['l']))

print('{}Seu nome com letras maiúsculas é: {}{}{}.'.format(cor['cyan_bold'], cor['red_bold'],
                                                           maiuscula, cor['l']))

print('{}Seu nome tem um total de {}{} letras{}.'.format(cor['cyan_bold'], cor['red_bold'],
                                                         letras_total, cor['l']))

print('{}O seu primeiro nome tem um total de {}{} letras{}.'.format(cor['cyan_bold'], cor['red_bold'],
                                                                    letras_primeiro, cor['l']))
