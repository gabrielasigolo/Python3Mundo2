mais_barato_nome = ''
maisdemil = mais_barato = soma = contador = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Preço: R$'))
    soma += preço
    contador += 1
    if preço > 1000:
        maisdemil += 1
    if contador == 1 or preço < mais_barato:
        mais_barato = preço
        mais_barato_nome = nome
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print(f"O total da compra foi: R$ {soma:.2f}")
print(f'Temos {maisdemil} produtos que custam mais de mil reais.')
print(f'E o produto mais barato custa {mais_barato:.2f} e é o {mais_barato_nome}')

