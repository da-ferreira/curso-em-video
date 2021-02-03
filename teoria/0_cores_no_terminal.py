'''

Código ANSI de escape sequence

\033[0;33;44m
o primeiro valor no colchete é o estilo do texto(negrito, itálico){style}.
o segundo valor no colchete é a cor do texto.{text color}
o terceiro valor no colchete é a cor de fundo{background color}.

Os códigos que vão funcionar melhor no terminal para o PYTHON são:

STYLE {estlo do texto}

0 = none (sem estilo nenhum), pode colocar 0 ou não colocar nada.
1 = bold (negrito)
4 = underline (sublinhado)
7 = negative (inverte), o que for para fundo vai para letra e o que for para letra vai para fundo.

TEXT {cor do texto}

30 = white (branco)
31 = red (vermelho)
32 = green (verde)
33 = yellow (amarelo)
34 = blue (azul)
35 = roxo (magenta)
36 = cyan (ciano)
37 = grey (cinza)

BACKGROUND (cor de fundo)

40 = white (branco)
41 = red (vermelho)
42 = green (verde)
43 = yellow (amarelo)
44 = blue (azul)
45 = magenta
46 = cyan (ciano)
47 = grey (cinza)

\033[m = configuração padrão do terminal
\033[7;30 m = o 7 é negativo, então, o 30(letra branca) fica preto e o 7 fica branco.

'''

print('\033[1;31;43mOlá, Mundo!\033[m')

print('\033[4;30;45mOlá, Mundo!\033[m')

print('\033[7;30mOlá, Mundo!\033[m') # inverteu o fundo para branco e a letra para preto

print('\033[7;33;44mOlá, Mundo!\033[m') # invertido

print('\033[33;44mOlá, Mundo!\033[m')

print()

a = 3
b = 5
print('Os valores são \033[32m{} \033[me \033[31m{}\033[m!!'.format(a, b))

print()

nome = 'David'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;33m', nome, '\033[m')) # outra forma de fazer

print() # outra forma de fazer abaixo:

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'} # dicionário

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
