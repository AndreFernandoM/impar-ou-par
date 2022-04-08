from pprint import pprint
from numpy import random, true_divide

a = True
print("-------Jogo de impar ou par-------\n")

while True :
    op=input('> Escolha par ou impar: ')
    op = op.lower()

    if op == 'impar' or op == 'par':
        num=int(input('Escolha um número de 0 a 10 para jogar: '))
        
        if num > 10:
            print('Burrão. É só até 10')
                
        else:
            break
    else:
        print("Burrão. É par ou impar")
        
op2= random.randint(10)
op2 = int(op2)
num = int(num)
soma=(op2+num)

print(f'Você escolheu {op} e o bot escolheu {op2}\n')

if op == 'par':

    if soma % 2 == 0:
        print("-------Parabéns você ganhou-------")

    else:
        print("Otario perdeu pra bot KKKKKKKKKKK")

elif op == 'impar':
    if soma % 2 != 0:
        print('-------Parabéns você ganhou-------')
    else:
        print('Otario perdeu pra bot KKKKKKKKKKK')

else:
    print("Escreve direito otario")
