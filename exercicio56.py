somaIdades = somaMulheres = maioridadehomem = 0
nomevelho = ''
for c in range(0, 4):
    print('='* 4, '{}º PESSOA'.format(c+1), '=' * 4)
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite seu sexo (F ou M): ')
    somaIdades += idade
    mediaIdades = somaIdades / 4
    if c == 0 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        somaMulheres += 1
print('\033[33m-=\033[m'*20)
print('A média de idades é {:.1f}'.format(mediaIdades))
print('Existindo {} mulheres com menos de 20 anos'.format(somaMulheres))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem, nomevelho))
print('\033[33m-=\033[m'*20)








