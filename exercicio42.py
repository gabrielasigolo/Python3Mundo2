r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

#Colocando as substrações no método abs para tirar o módulo
modulo1 = abs(r2 - r3)
modulo2 = abs(r1 - r3)
modulo3 = abs(r1 - r2)

if (modulo1) < r1 < (r2 + r3) and (modulo2) < r2 < (r1 + r3) and (modulo3) < r3 < (r1 + r2):
    print('É possivel formar um triângulo! ')
    if r1 == r2 == r3:
        print("E esse é um triângulo equilátero!")
    elif r1 == r2 or r1 == r3:
        print("Esse é um triângulo isósceles")
    else:
        print("É um triângulo escaleno!")
else:
    print('Não é possivel formar um triângulo.')