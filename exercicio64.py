num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        cont += 1
        soma += num
print('FIM! A soma dos {} números inseridos foi {}'.format(cont, soma))
