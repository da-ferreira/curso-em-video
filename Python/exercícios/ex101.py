
def voto(nascimento):
    from datetime import datetime
    idade = datetime.today().year - nascimento

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


print('\n -=-=- VOTAÇÃO -=-=-')
ano_nascimento = voto(int(input('\nEm que ano você nasceu? ')))
print(ano_nascimento)
