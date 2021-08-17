from random import randint
from time import sleep


print('\033[0;33;40m-=-\033[m' * 20)
print('    TENTE DESCOBRIR O NÚMERO QUE O PC ESTÁ PENSANDO')
print('\033[0;33;40m-=-\033[m' * 20)

numero_aleatorio = randint(0, 10)
palpites = 0
acertou = False
while not acertou:
    numero = int(input('\033[0;31mDigite um número inteiro entre 0 e 10: '))
    print('\033[1;32mPROCESSANDO...')
    palpites += 1
    sleep(2)

    if numero == numero_aleatorio:
        acertou = True
    else:
        if numero < numero_aleatorio:
            print('Mais...Tente mais uma vez.')
        elif numero > numero_aleatorio:
            print('Menos...Tente mais uma vez.')
print('\033[0;36;40mParabéns! O número era {}, acertou com {} palpites\033[m'.format(numero_aleatorio, palpites))

