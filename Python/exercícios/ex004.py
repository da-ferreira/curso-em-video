cor = {
       'limpar': '\033[m',
       'roxo_negrio': '\033[1;35m',
       'azul': '\033[34m',
       'verde_negrito': '\033[1;32m'
       }

print('\n{}Informações sobre um valor{}\n'.format(cor['roxo_negrio'], cor['limpar']))

valor = input('Digite algo: ')
print()
print('Pertence a qual tipo primito? {}{}{}\n'.format(cor['verde_negrito'], type(valor), cor['limpar']))
print('Só tem espaço em branco? {}{}{}\n'.format(cor['verde_negrito'], valor.isspace(), cor['limpar']))
print('É um número? {}{}{}\n'.format(cor['verde_negrito'], valor.isnumeric(), cor['limpar']))
print('É uma letra? {}{}{}\n'.format(cor['verde_negrito'], valor.isalpha(), cor['limpar']))
print('É alfanumérico? {}{}{}\n'.format(cor['verde_negrito'], valor.isalnum(), cor['limpar']))
print('Está somente em letras maiúsculas? {}{}{}\n'.format(cor['verde_negrito'], valor.isupper(), cor['limpar']))
print('Está somente em letras minúsculas? {}{}{}\n'.format(cor['verde_negrito'], valor.islower(), cor['limpar']))
print('Está capitalizado? {}{}{}\n'.format(cor['verde_negrito'], valor.istitle(), cor['limpar']))
