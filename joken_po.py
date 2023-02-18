import random

escolha1 = ['papel', 'tesoura', 'pedra']
escolha1 = random.choice(escolha1)
print('=-==-===-==== PEDRA, PAPEL, TESOURA ====-===-==-=\n\n')
escolha2 = input('Faça a sua jogada: Pedra, Papel ou Tesoura\n').lower()
print('\n' * 100)
if escolha1 == escolha2:
    print('Você escolheu: {}\nEscolha do computador: {}\n\nEMPATE !!'.format(escolha2, escolha1))
    
elif escolha1 == 'papel' and escolha2 == 'tesoura':
    print('Você escolheu: {}\nEscolha do computador: {}\n\nVOCÊ VENCEU !!'.format(escolha2, escolha1))
    
elif escolha1 == 'papel' and escolha2 == 'pedra':
    print('Você escolheu: {}\nEscolha do computador: {}\n\nVOCÊ PERDEU :( !!'.format(escolha2, escolha1))

elif escolha1 == 'tesoura' and escolha2 == 'pedra':
    print('Você escolheu: {}\nEscolha do computador: {}\n\nVOCÊ VENCEU !!'.format(escolha2, escolha1))
    
elif escolha1 == 'tesoura' and escolha2 == 'papel':
    print('Você escolheu: {}\nEscolha do computador: {}\n\nVOCÊ PERDEU :( !!'.format(escolha2, escolha1))
    
elif escolha1 == 'papel' and escolha2 == 'tesoura':
    print('Você escolheu: {}\nEscolha do computador: {}\n\nVOCÊ VENCEU !!'.format(escolha2, escolha1))
elif escolha1 == 'papel' and escolha2 == 'pedra':
    print('Você escolheu: {}\nEscolha do computador: {}\n\nVOCÊ PERDEU :( !!'.format(escolha2, escolha1))

elif escolha1 == 'pedra' and escolha2 == 'papel':
    print('Você escolheu: {}\nEscolha do computador: {}\n\nVOCÊ VENCEU !!'.format(escolha2, escolha1))
    
elif escolha1 == 'pedra' and escolha2 == 'tesoura':
    print('Você escolheu: {}\nEscolha do computador: {}\n\nVOCÊ PERDEU :( !!'.format(escolha2, escolha1))
    
else:
    print(f'Você digitou algo inválido.')