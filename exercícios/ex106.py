from time import sleep

cor = {
    'limpa': '\033[m',
    'azul': '\033[1;30;46m',
    'vermelho': '\033[1;30;41m',
    'branco': '\033[1;7;30m',
    'roxo': '\033[1;30;45m'
}


def mensagem(texto, color, caractere='~'):
    """
    :param texto: O texto que vai ser mostrado na mensagem
    :param color: A cor do texto.
    :param caractere: Opcional, caractere que enfeita o texto.
    :return: sem retorno
    """
    print(cor[color] + caractere * (len(texto) + 2))
    print(f' {texto} ')
    print(caractere * (len(texto) + 2))


while True:
    mensagem(f'SISTEMA DE AJUDA PyHELP', 'azul')
    comando = input(f'{cor["limpa"]}Função ou Biblioteca > ').strip().lower()

    if comando == 'fim':
        break
    sleep(0.5)
    mensagem(f"Acessando o manual do comando '{comando}'", 'vermelho', '¬')
    sleep(0.8)

    print(cor['branco'])
    help(comando)
    sleep(1)

mensagem('<< ATÉ LOGO! >>', 'roxo', '^')
