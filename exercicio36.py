casa = float(input("Digite o valor da casa: "))
salário = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos será feito o pagamento: "))

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print("Para pagar uma casa de R$ {:.2f} em {} anos".format(casa, anos), end='')
print(" a prestação será de R${:.2f}".format(prestação))

if prestação <= mínimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo negado!")
