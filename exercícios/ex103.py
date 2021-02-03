
def ficha(nome='<desconhecido>', gols=0):  # <- parâmetros opcionais.
    print('\n ¬¬¬¬ DADOS DO JOGADOR ¬¬¬¬ ')
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('\n ¬¬¬ CADASTRO DO JOGADOR ¬¬¬')
nome_jogador = input('Nome do jogador: ').title().strip()
num_gols = input('Número de gols: ').strip()

if not num_gols.isnumeric():
    num_gols = 0

if nome_jogador == '' and num_gols == '':  # <- Ausência de nome e gols.
    ficha()
elif nome_jogador == '':  # <- Ausência de nome.
    ficha(gols=num_gols)
elif num_gols == '':  # <- Ausência de gols.
    ficha(nome=nome_jogador)
else:
    ficha(nome_jogador, num_gols)
