listaPesos = []
for c in range(0, 5):
    peso = float(input('Peso da {}º pessoa: '.format(c+1)))
    listaPesos.append(peso)
print('O maior peso foi {:.1f} e o menor {:.1f}'.format(max(listaPesos), min(listaPesos)))
