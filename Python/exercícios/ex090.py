
aluno = dict()

aluno['Nome'] = input('\nNome do aluno: ').title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado(a)'
elif 7 > aluno['Média'] >= 5:  # <- Média menor que 7 e maior ou igual a 5.
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'

print()
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
