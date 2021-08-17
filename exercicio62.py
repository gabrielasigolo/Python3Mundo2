primeiroTermo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão: '))
total = 0
cont = 1
termo = primeiroTermo
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão terminada com {} termos mostrados'.format(total))
