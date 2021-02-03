from datetime import date

print('\n -=-=- CADASTRO DO TRABALHADOR -=-=- \n')

trabalhador = dict()

trabalhador['Nome'] = input('Nome: ').title()

nascimento = int(input('Ano de nascimento: '))
trabalhador['Idade'] = f'{date.today().year - nascimento} anos'

trabalhador['Ctps'] = int(input('Carteira de trabalho [ 0 caso não possuir ]: '))

if trabalhador['Ctps'] != 0:  # <- Se tiver CTPS.
    trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Valor do salário: R$ '))

    aposentadoria = (trabalhador['Ano de contratação'] - nascimento) + 35  # Tempo para se aposentar.
    trabalhador['Idade para aposentadoria'] = f'{aposentadoria} anos'
print('-=-' * 18, '\n')

print('DADOS DO TRABALHADOR: \n')
for key, valor in trabalhador.items():
    print(f'{key}: {valor}')
