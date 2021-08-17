from datetime import  date

anoNasci = int(input('Em que ano você nasceu? '))
now = date.today()
ano = now.strftime('%Y')
anoAtual = int(ano)

idade = anoAtual - anoNasci
if idade < 18:
    saldo = 18 - idade
    print("Ainda é cedo! Você só irá se alistar daqui {} anos".format(saldo))
    print("A seu ano de alistamento será em {}".format(anoAtual + saldo))
elif idade == 18:
    print("Já chegou sua hora de se alistar ao serviço militar!")
else:
    saldo = idade - 18
    print("Já passou a hora de se alistar, você está atrasado {} anos".format(saldo))
    print("Sua data de alistamento foi em {}".format(anoAtual - saldo))
