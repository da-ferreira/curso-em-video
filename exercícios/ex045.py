from random import choice
from time import sleep

print()
print('-=-' * 8)
print('PEDRA, PAPEL & TESOURA')
print('-=-' * 8)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(lista)


def jokenpo():
    escolha = int(input('\nESCOLHA SUA JOGADA:'
                        '\n[ 1 ] para escolher PEDRA.'
                        '\n[ 2 ] para escolher PAPEL.'
                        '\n[ 3 ] para escolher TESOURA.\n'))

    #  Se o usuário escolher PEDRA.
    if (escolha == 1) and (pc == 'PEDRA'):
        print('\nVocê escolheu PEDRA!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nEMPATOU!\nVocê e o computador escolheram pedra.')
    elif (escolha == 1) and (pc == 'PAPEL'):
        print('\nVocê escolheu PEDRA!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nO COMPUTADOR VENCEU!\nEle escolheu papel.')
    elif (escolha == 1) and (pc == 'TESOURA'):
        print('\nVocê escolheu PEDRA!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nVOCÊ VENCEU!\nO computador escolheu tesoura.')

    #  Se o usuário escolher PAPEL.
    elif (escolha == 2) and (pc == 'PEDRA'):
        print('\nVocê escolheu PAPEL!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nVOCÊ VENCEU!\nO computador escolheu pedra.')
    elif (escolha == 2) and (pc == 'PAPEL'):
        print('\nVocê escolheu PAPEL!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nEMPATOU!\nVocê e o computador escolheram papel.')
    elif (escolha == 2) and (pc == 'TESOURA'):
        print('\nVocê escolheu PAPEL!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nVOCÊ PERDEU!\nO computador escolheu tesoura.')

    #  Se o usuário escolher TESOURA.
    elif (escolha == 3) and (pc == 'PEDRA'):
        print('\nVocê escolheu TESOURA!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nVOCÊ PERDEU!\nO computador escolheu pedra.')
    elif (escolha == 3) and (pc == 'PAPEL'):
        print('\nVocê escolheu TESOURA!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nVOCÊ VENCEU!\nO computador escolheu papel')
    elif (escolha == 3) and (pc == 'TESOURA'):
        print('\nVocê escolheu TESOURA!')
        print('\nJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!')
        sleep(1)
        print('\nEMPATOU!\nVocê e o computador escolheram tesoura.')


desafio = input('\nCOMPUTADOR: Vamos jogar pedra, papel e tesoura?\n'
                '\nQuer jogar contra o computador?\n'
                'Escolha digitando [SIM] ou [NÃO].\n').lower().strip()

if desafio == 'sim':
    jokenpo()
    jogar_novamente = input('\nQuer jogar novamente?'
                            '\nEscolha digitando [sim] ou [não].\n').lower().strip()
    if jogar_novamente == 'sim':
        jokenpo()
    else:
        print('\nMuito obrigado por ter jogado!\nVolte em qualquer momento e jogue novamente :)')

else:
    print('Ok, tenha um bom dia!')
