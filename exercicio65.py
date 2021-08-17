num = soma = count = 0
cont = None
numeros = []
while cont != 0:
    num = int(input('Digite um número: '))
    numeros.append(num)
    soma += num
    count += 1
    cont = int(input('''Você deseja continuar ou parar aqui? 
                        [0] Parar
                        [1] Continuar '''))
print('A média dos números foi {:.1f}, o maior número foi {} e o menor {}'.format(soma/count, max(numeros), min(numeros)))

