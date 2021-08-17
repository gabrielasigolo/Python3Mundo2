sexo = ''
while all([sexo != 'F', sexo != 'M']):
    sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
    if all([sexo != 'F', sexo != 'M']):
        print('Sexo inválido! Por favor, tente novamente!')
print('Sexo {} registrado com sucesso'.format(sexo))


