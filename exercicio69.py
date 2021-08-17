n = maisde18 = homens = mulheres20 = 0
cont = ''

while True:
    n += 1
    print(f'{n}º PESSOA')
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    if idade > 18:
        maisde18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    cont = str(input('Deseja continuar? [S/N]')).upper()
    if cont == 'N':
        break
    print('~'*20)
print(f'Existem {maisde18} pessoas com mais de 18 anos, ' if maisde18 > 1 else f'Existe {maisde18} pessoa com mais de 18 anos,', end=' ')
print(f'sendo que {homens} homens foram cadastrados ' if homens > 1 else f'sendo que {homens} homem foi cadastrado ')
print(f'E existem {mulheres20} mulheres com menos de 20 anos' if mulheres20 > 1 else f'E existe {mulheres20} mulher com menos de 20 anos')




