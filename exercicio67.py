tabuada = 1
while tabuada > 0:
    tabuada = int(input('Digite um número: '))
    print('=' * 30)
    c = 0
    if tabuada < 0:
        break
    while c < 10:
        c += 1
        print(f'{c} x {tabuada} = {c * tabuada}')
    print('='*30)
print('FIM!')

