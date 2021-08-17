primeiroTermo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão: '))
décimo = primeiroTermo + (10-1) * razao
cont = ''
i = primeiroTermo
while i < décimo + razao:
    i = i + razao
    print(i)
print('PAUSA')

