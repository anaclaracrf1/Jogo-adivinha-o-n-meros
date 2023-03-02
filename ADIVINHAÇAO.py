
import random

print('\033[34m-\033[m'*50)
print('Bem vindo ao jogo da adivinhação!')
print('\033[34m-\033[m'*50)

from time import sleep
print(f'\033[34mJogo adivinhe o número\033[m')
sleep(1.25)
print(f'\033[35mO computador vai pensar em um número de 0 a 20.\033[m')
sleep(1.25)
print(f'\033[34mO jogo pode ter até 4 jogadores!\033[m')
sleep(1.25)
print(f'\033[34mTente adivinhar:\033[m')
sleep(1.25)

print('[1]Fácil - 9 tentativas '
      '\n[2]Médio - 6 tentativas '
      '\n[3]Difícil - 3 tentativas')
tentativas = 0
totaldetentativas = 1
level = int(input('Escolha um nível:'))
totaldepontos = 100

if level == 1:
    totaldetentativas = 9
if level == 2:
    totaldetentativas = 6
if level == 3:
    totaldetentativas = 3

numero_secreto = int(random.randrange(20))
print('\033[34m-\033[m'*50)
chute = int(input('\033[4:34mChute um número [entre 1 e 20]:\033[m'))

while tentativas != totaldetentativas:

    if chute < 1 or chute > 20:
        print('O CHUTE DEVE SER ENTRE 1 E 20***')

    if chute != numero_secreto:
        tentativas += 1
        print(f'Tentativa \033[34m{tentativas}\033[m de \033[34m{totaldetentativas}\033[m.\nVocê \033[31mnão\033[m acertou!\nTente novamente...')

        if chute > numero_secreto:
            print('\033[35mDica\033[m: seu chute foi muito alto.')

        elif chute < numero_secreto:
            print('\033[35mDica:\033[mseu chute foi muito baixo.')

        pontosfinais = totaldepontos - chute
        totaldepontos = pontosfinais
        print(f'Você está com {pontosfinais} pontos após essa tentativa.')

        print('\033[34m-\033[m' * 50)
        chute = int(input('\033[4:34mChute um número:\033[m'))

    elif chute == numero_secreto:
        tentativas+= 1
        print(f'\033[32mParabéns!! Você acertou em {tentativas} tentativas.')
        print(f'Total de pontos feitos {pontosfinais} pontos!!')
        break