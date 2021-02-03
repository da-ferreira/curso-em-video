from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    sleep(1.5)
    if inicio >= fim:  # <- A contagem é decrescente.
        fim -= 1
        if passo > 0:
            passo *= -1

    else:  # <- A contagem é crescente.
        fim += 1
        if passo < 0:  # Começando em negativo e indo para positivo com passo negativo
            passo *= -1

    for i in range(inicio, fim, passo):
        print(i, end=' ')
        sleep(0.4)
    print('FIM!')
    print('-=-' * 15)


print('-=-' * 15)
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')

start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

print('-=-' * 15)
contador(start, end, step)  # <- Função passando os parâmetros.

