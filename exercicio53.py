frase = str(input('Digite uma frase: ')).strip().upper()

semEspacos = ''.join(frase.split())
inverso = ''
for letra in range(len(semEspacos) - 1, -1, -1):
    inverso += semEspacos[letra]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == semEspacos:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')




