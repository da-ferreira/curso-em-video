
def metade(preco=0, formatado=False):
    """
    -> Função que para pegar a metade de um valor.
    :param preco: (Opcional) O valor.
    :param formatado: (Opcional) se deseja visualizar o valor formatado como moeda.
    :return: A metade do valor.
    """
    resultado = preco / 2
    return resultado if not formatado else moeda(resultado)


def dobro(preco=0, formatado=False):
    """
    -> Função que mostra o dobro de um valor.
    :param preco: (Opcional) o valor.
    :param formatado: (Opcional) se deseja visualizar o valor formatado como moeda.
    :return: O dobro do valor.
    """
    resultado = preco * 2
    return resultado if not formatado else moeda(resultado)


def aumentar(preco=0, porcentagem=0, formatado=False):
    """
    -> Função que aumenta um valor em porcentagem.
    :param preco: (Opcional) o valor.
    :param porcentagem: (Opcional) a porcentagem que deseja-se aumentar.
    :param formatado: (Opcional) se deseja visualizar o valor formatado como moeda.
    :return: O valor aumentado conforme sua porcentagem.
    """
    resultado = preco + ((preco * porcentagem) / 100)
    return resultado if not formatado else moeda(resultado)


def diminuir(preco=0, porcentagem=0, formatado=False):
    """
    -> Função que diminui um valor conforme uma porcentagem.
    :param preco: (Opcional) o valor.
    :param porcentagem: (Opcional) a porcentagem que deseja-se reduzir.
    :param formatado: (Opcional)  se deseja visualizar o valor formatado como moeda.
    :return: O valor reduzido conforme sua porcentagem.
    """
    resultado = preco - ((preco * porcentagem) / 100)
    return resultado if not formatado else moeda(resultado)


def moeda(preco=0, simbolo='R$'):
    """
    -> Função que formata um valor como moeda.
    :param preco: O valor a ser formatado.
    :param simbolo: (Opcional) a sigla da moeda.
    :return: O valor formatado.
    """
    return f'{simbolo}{preco :>.2f}'.replace('.', ',')


def resumo(preco=0, acrescimo=10, decrescimo=5):
    """
    :param preco: Recebe um valor preço qualquer.
    :param acrescimo: (Opcional) porcentagem para aumentar.
    :param decrescimo: (Opcional) porcentagem para diminuir.
    :return: Sem retorno.
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)

    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{acrescimo}% de aumento:  \t{aumentar(preco, acrescimo, True)}')
    print(f'{decrescimo}% de redução:  \t{diminuir(preco, decrescimo, True)}')

    print('-' * 30)
