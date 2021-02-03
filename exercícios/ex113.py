
def leiaInt(mensagem=''):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mUsuário decidiu não informar o número.')
            numero = 0
            break
        else:
            break
    return numero


def leiaFloat(mensagem=''):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mUsuário decidiu não informar o número.\033[m')
            numero = 0
            break
        else:
            break
    return numero


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {inteiro} e o número real {real}')
