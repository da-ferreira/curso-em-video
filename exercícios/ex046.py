import emoji
from time import sleep

print('-=' * 10)
print('CONTAGEM REGRESSIVA')
print('-=' * 10)

for contar in range(10, -1, -1):
    print(contar)
    sleep(1)
print(emoji.emojize(':collision:' * 8))
print(emoji.emojize(':skull: BOOOOOM :skull:'))
print(emoji.emojize(':collision:' * 8))
