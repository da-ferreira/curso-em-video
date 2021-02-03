
palavras = (
    'python', 'aprender', 'viajar', 'morar',
    'casar', 'celular', 'computador', 'casa',
    'garrafa', 'mercado', 'apartamento', 'flor',
)
print('\nVogais de cada palavra abaixo:')

for i in palavras:
    print(f'\npalavra {i.upper()} tem: ', end='')
    for letras in i:  # <- Cada string é uma tupla/lista, portanto, da pra listar cada elemento dela.
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
