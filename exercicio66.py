num = soma = cont = 0

while True:
    num = int(input('Digite um número (999 para parar): '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f'FIM! A soma dos {cont} números inseridos foi {soma}')
