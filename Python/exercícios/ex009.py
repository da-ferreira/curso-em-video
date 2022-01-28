print('\n\033[1;31mTABUADA')

num = int(input('\nDigite um número para ver sua tabuada:\033[m '))

print(f'\033[1;33mTabuada do {num}:\033[m')
print('\033[7;30m-\033[m' * 14)
print(f'\033[1;35m {num} x  1 = {num * 1}\n {num} x  2 = {num * 2}\n {num} x  3 = {num * 3}'
      f'\n {num} x  4 = {num * 4}\n {num} x  5 = {num * 5}')
print(f' {num} x  6 = {num * 6}\n {num} x  7 = {num * 7}'
      f'\n {num} x  8 = {num * 8}\n {num} x  9 = {num * 9}')
print(f' {num} x 10 = {num * 10}\033[m')
print('\033[7;30m-\033[m' * 14)
