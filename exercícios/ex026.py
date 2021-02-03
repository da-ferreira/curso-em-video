print('\033[4;35mPrimeira e última aparição do "A".\033[m')

frase = str(input('\n\033[1;34mDigite uma frase: \033[1;36m')).lower().strip()

vezes = frase.count('a')
primeira = frase.find('a')+1
ultima = frase.rfind('a')+1

print('\nA letra "a" aparece {} vezes na frase.'.format(vezes))
print('A primeira aparição dela está na posição {}.'.format(primeira))
print('A última aparição dela está na posição {}.'.format(ultima))
