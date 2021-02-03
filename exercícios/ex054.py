from datetime import date

print('\nGRUPO DE MAIORIDADE\n')  # Pessoas com mais de 21 anos.

maioridade = 0
menor = 0

for contar in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(contar)))
    idade = date.today().year - ano
    if idade >= 21:
        maioridade += 1
    elif idade < 21:
        menor += 1
print('\nDentre as 7 pessoas informadas acima:\n{} são maiores de idade.'
      '\n{} ainda não atingiram a maioridade.'.format(maioridade, menor))
