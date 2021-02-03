"""
-=-=- ERROS E EXCEÇÕES -=-=-
"""

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:  # <- Informando qual foi o erro cometido.
    print(f'Problema encontrado foi {erro.__context__}')  # <- Mostra a classe do erro (EX: <class 'ValueError'>).
else:
    print(f'O resultado é {r :.1f}')
finally:
    print('Volte sempre! Muito obrigado')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'O resultado é {r :.1f}')

finally:
    print('Volte sempre! Muito obrigado')
