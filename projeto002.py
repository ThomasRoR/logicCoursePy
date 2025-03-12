#Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

#O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.
 #Método 50's para montar um algorítimo:

#Analise criticamente o problema e descubra:
#(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

#1. Quais são os dados de entrada necessários?
# o  chute e o valor aleatorio
#2. O que devo fazer com estes dados?
# comparalos, se igual finalizar, se errar informar se o chute foi acima ou abaixo.
#3. Quais são as restrições deste problema?
# valores deve ser de 1 a 10
#4. Qual é o resultado esperado?
# nova tentativa ou mensagem de acerto
#5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?

import random

valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int(input('chute um novo valor entre: 1 e 10: '))
    if chute > valor_aleatorio:
        print('menor')
    elif chute < valor_aleatorio:
        print('maior')
    elif chute == valor_aleatorio:
        print('Voce acerto')
        acertou = True