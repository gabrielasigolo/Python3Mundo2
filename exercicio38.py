num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print('O primeiro valor é \033[0;31mmaior\033[m')
elif num2 > num1:
    print('O segundo valor é \033[0;31mmaior\033[m')
else:
    print('Não existe valor maior, os dois são \033[0;34miguais\033[m')