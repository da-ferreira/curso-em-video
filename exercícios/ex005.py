cor = {
       'negativo': '\033[7;30m',
       'limpar': '\033[m'
       }

print('\n{}Sucessor e antecessor de um número{}'.format(cor['negativo'], cor['limpar']))

n1 = int(input('\nDigite um número: '))
suce = n1 + 1
antece = n1 - 1
print(f'O sucessor é \033[33m{suce}\033[m!\nO antecessor é \033[033m{antece}\033[m!')
