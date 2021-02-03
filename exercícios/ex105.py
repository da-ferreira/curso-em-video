
def notas(*nota, situacao=False):
    """
    -> Função que analisa nota e situação de vários alunos.
    :param nota: recebe as notas(pode ser várias).
    :param situacao: Valor opcional, indicando se deve ou não mostrar adicionar a situação.
    :return: Dicionário com várias informações.
    """
    dicionario = {'Total': len(nota), 'Maior': max(nota), 'Menor': min(nota),
                  'Média': round(sum(nota) / len(nota), 1)}

    if situacao:
        if dicionario['Média'] >= 7:
            dicionario['Situação'] = 'BOA'
        elif 5 <= dicionario['Média'] < 7:
            dicionario['Situação'] = 'RAZOÁVEL'
        else:
            dicionario['Situação'] = 'RUIM'
    return dicionario


resposta = notas(9, 10, 5.5, 2.5, 9, 8.5, situacao=True)
print(resposta)
