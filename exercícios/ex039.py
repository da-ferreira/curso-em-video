from datetime import date

# Para pegar datas
print('\nALISTAMENTO MILITAR')


def alistamento():
    ano = int(input('\nEm que ano você nasceu? '))
    ano_atual = date.today().year  # Para saber o ano atual da máquina.
    idade = ano_atual - ano
    print('\nQuem nasceu em {} tem {} anos em {}.'.format(ano, idade, ano_atual))

    if idade < 18:
        print('Sua hora de se alistar ainda não chegou.'
              '\nMas fique atento, falta apenas {} ano(s) para poder se alistar.'
              '\nSeu Alistamento será em {}.'.format((18 - idade), (ano + 18)))
    elif idade == 18:
        print('\nÉ hora de se alistar no exército.'
              '\nVá até a junta militar mais próxima e realize seu alistamento.')
    elif idade > 18:
        print('\nVocê deveria ter se alistado há {} anos.'
              '\nSeu alistamento foi em {}.'.format(ano_atual - (ano + 18), (ano + 18)))


sexo = int(input('\nQual seu sexo?\n\n[ 1 ] PARA MASCULINO\n[ 2 ] PARA FEMININO\n'))

if sexo == 1:
    alistamento()
elif sexo == 2:
    print('Você não precisa fazer alistamento militar obrigatório.')
else:
    print('ENTRADA INVÁLIDA. Tente novamente. ')
