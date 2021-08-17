import time
import random

jogada = str(input("Pedra, papel ou tesoura?")).lower().strip()

lista = ['pedra', 'papel', 'tesoura']
escolha = random.choice(lista)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!')
print()


if jogada == 'pedra' and escolha == 'papel':
    print("COMPUTADOR: Pedra")
    print("VOCÊ: Papel")
    print("Parabéns! Você ganhou! \U0001F600")
elif jogada == 'pedra' and escolha == 'tesoura':
    print("COMPUTADOR: Pedra")
    print("VOCÊ: Tesoura")
    print("Você perdeu \U0001F614")
elif jogada == 'papel' and escolha == 'pedra':
    print("COMPUTADOR: Papel")
    print("VOCÊ: Pedra")
    print("Você perdeu \U0001F614")
elif jogada == 'papel' and escolha == 'tesoura':
    print("COMPUTADOR: Papel")
    print("VOCÊ: Tesoura")
    print("Parabéns! Você ganhou! \U0001F600")
elif jogada == 'tesoura' and escolha == 'papel':
    print("COMPUTADOR: Tesoura")
    print("VOCÊ: Papel")
    print("Você perdeu \U0001F614")
elif jogada == 'tesoura' and escolha == 'pedra':
    print("COMPUTADOR: Pedra")
    print("VOCÊ: Tesoura")
    print("Você perdeu \U0001F614")
elif jogada == escolha:
    print("Empatou")

