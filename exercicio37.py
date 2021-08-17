num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
 [1] Binário
 [2] Octal 
 [3] Hexadecimal''')
opção = int(input('Sua opção: '))

if opção == 1:
    print("{} convertido para BINÁRIO é igual {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para OCTAL é igual {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} convertido para HEXADECIMAL é igual {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida!")

