n = int(input('Digite um número: '))
tot = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é \033[35mprimo\033[m!')
else:
    print('E por isso ele NÃO É PRIMO!')

