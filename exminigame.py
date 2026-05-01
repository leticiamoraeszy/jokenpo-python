from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções:'
' [0] - PEDRA'
' [1] - PAPEL '
' [2] - TESOURA ')
jogador = int(input('Qual vai ser a sua jogada?: ')) # Jogador seleciona número
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-=-'*10)
print('Jogador escolheu: {}'.format(itens[jogador]))
print('O computador escolheu: {}'.format(itens[computador]))
print('-=-'*10)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('\033[0;31mEMPATE\033')
    elif jogador == 1:
        print('\033[0;34mJOGADOR VENCE\033')
    elif jogador == 2:
        print('\033[0;32mCOMPUTADOR VENCE\033')
    else:
        print('JOGADA INVÁLIDA')
elif computador ==1: #computador jogou PAPEL
    if jogador == 0:
        print('\033[0;32mCOMPUTADOR VENCE\033')
    elif jogador == 1:
        print('\033[0;31mEMPATE\033')
    elif jogador == 2:
        print('\033[0;34mJOGADOR VENCE\033')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('\033[0;34mJOGADOR VENCE\033')
    elif jogador == 1:
        print('\033[0;32mCOMPUTADOR VENCE\033')
    elif jogador == 2:
        print('\033[0;31mEMPATE\033')
    else:
        print('JOGADA INVÁLIDA')
