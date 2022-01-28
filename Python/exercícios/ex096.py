
def área(larg, compri):
    resultado = larg * compri
    print(f'A área de um terreno {larg :.1f} x {compri :.1f} é de {resultado :.1f}m².')


def mensagem(texto):
    print('-=-' * 15)
    print(f'{texto :^45}')
    print('-=-' * 15)


mensagem('ÁREA DE UM TERRENO')
largura = float(input('\nLargura do terreno(m): '))
comprimento = float(input('Comprimento do terreno(m): '))
área(largura, comprimento)  # <- Chamando a função.
