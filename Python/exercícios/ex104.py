
def leiaInt(mensagem=''):
    veracidade = 0  # <- Para saber se o tamanho do número tem o mesmo que a variável.
    while True:
        numero = input(mensagem).strip()
        numero = numero.replace(',', '.')
        for i in numero:
            if i in '0123456789.':
                veracidade += 1
        if veracidade == len(numero) and numero != '':
            return float(numero)
        print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        veracidade = 0


number = leiaInt('\nDigite um número: ')
print(f'\nVocê digitou o número {number}')
