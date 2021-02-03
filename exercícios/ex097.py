
def escreva(texto, caractere):
    print()
    print(caractere * (len(texto) + 2))
    print(f' {texto} ')
    print(caractere * (len(texto) + 2))
    print()


caracteres = {
    1: '-',
    2: '~',
    3: '=',
    4: '"',
    5: '*',
    6: '.',
    7: '+',
    8: '¬',
    9: '§',
    10: '°'
}


while True:
    mensagem = input('\nEscreva uma mensagem/título: ').upper().strip()

    while True:
        modo = int(input('\nEscolha o modo que deseja enfeitar seu texto:'
                         '\n    [  1  ] com o caractere ----'
                         '\n    [  2  ] com o caractere ~~~~'
                         '\n    [  3  ] com o caractere ===='
                         '\n    [  4  ] com o caractere """"'
                         '\n    [  5  ] com o caractere ****'
                         '\n    [  6  ] com o caractere ....'
                         '\n    [  7  ] com o caractere ++++'
                         '\n    [  8  ] com o caractere ¬¬¬¬'
                         '\n    [  9  ] com o caractere §§§§'
                         '\n    [  10 ] com o caractere °°°°'
                         '\n>>> MODO: '))
        if modo in range(1, 11):
            break
        print(f'\nERROR! Não existe um modo com numeração {modo}.')

    escreva(mensagem, caracteres[modo])  # <- Escrevendo a mensagem.

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        print('Informe apenas S(sim) ou N(não).')
        continuar = input('Quer continuar [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('<< VOLTE SEMPRE >>')
