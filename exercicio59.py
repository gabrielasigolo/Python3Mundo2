num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

resp = ''
while resp != 5:
    print('''Que operação você deseja fazer com esses números? 
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos números
            [5] Sair do programa''')
    resp = int(input('ESCOLHA: '))
    if resp == 1:
        result = num1 + num2
        print('O soma dos dois números é {}'.format(result))
    elif resp == 2:
        result = num1 * num2
        print('O produto dos dois números é {}'.format(result))
    elif resp == 3:
        maiorNumero = num1
        if num2 > num1:
            maiorNumero = num2
        print('O maior número é {}'.format(maiorNumero))
    elif resp == 4:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
    elif resp == 5:
        break
    else:
        print('Escolha uma opção válida!')


