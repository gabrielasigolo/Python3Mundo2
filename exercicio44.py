preco = float(input("Qual é o preço do produto?"))
print("""\033[1;34mEscolha uma condição de pagamento abaixo:\033[m
\033[1;31m[1]\033[m À vista dinheiro/cheque: 10% de desconto
\033[1;31m[2]\033[m À vista no cartão: 5% de desconto
\033[1;31m[3]\033[m Em até 2x no cartão: preço normal
\033[1;31m[4]\033[m 3x ou mais no cartão: 20% de juros""")
resp = int(input("Resposta: "))

if resp == 1:
    total = preco - (preco * 0.1)
elif resp == 2:
    total = preco - (preco * 0.05)
elif resp == 3:
    total = preco
    parcelas = total / 2
    print("O seu produto será parcelada em 2x de {:.2f}".format(parcelas))
elif resp == 4:
    total = preco + (preco * 20/100)
    totalParc = int(input('Em quantas parcelas?'))
    parcela = total / totalParc
    print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(totalParc, parcela))
else:
    total = preco
    print('\033[0;31mOpção inválida!\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))

