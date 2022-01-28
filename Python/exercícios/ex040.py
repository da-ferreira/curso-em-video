print('\nMédia classica')

nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('\nA média é {:.1f}'.format(media))

if media < 5.0:
    print('\nO aluno está REPROVADO!\n:(')
elif (media >= 5.0) and (media <= 6.9):
    print('\nO aluno está em RECUPERAÇÃO!\n:O')
elif media >= 7.0:
    print('\nO aluno está APROVADO!\n:)')

