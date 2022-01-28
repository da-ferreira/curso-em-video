
expressao = input('Digite sua expressão: ')

if expressao.count('(') == expressao.count(')'):
    print('\nSua expressão está VÁLIDA!')
else:
    print('\nSua expressão está ERRADA!')
