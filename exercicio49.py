tabuada = int(input('Digite um número: '))
print('=-' * 5, 'TABUADA DO {}'.format(tabuada), '=-' * 5)
for c in range(1, 11):
    print('{} x {} = {}'.format(c, tabuada, c*tabuada))
