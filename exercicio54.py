from datetime import date

somaÑMaiores = 0
somaMaiores = 0
for c in range(0, 7):
    anoNasci = int(input('Digite o ano de nascimento: '))
    atual = date.today().year
    idade = atual - anoNasci
    if idade < 21:
        somaÑMaiores += 1
    elif idade >= 21:
        somaMaiores += 1
print('{} pessoas são maiores de idade e {} não são'.format(somaMaiores, somaÑMaiores))

