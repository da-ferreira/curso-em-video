
def metade(preco=0):
    resultado = preco / 2
    return resultado


def dobro(preco=0):
    resultado = preco * 2
    return resultado


def aumentar(preco=0, porcentagem=0):
    resultado = preco + ((preco * porcentagem) / 100)
    return resultado


def diminuir(preco=0, porcentagem=0):
    resultado = preco - ((preco * porcentagem) / 100)
    return resultado


def moeda(preco=0, simbolo='R$'):
    return f'{simbolo}{preco :>.2f}'.replace('.', ',')
