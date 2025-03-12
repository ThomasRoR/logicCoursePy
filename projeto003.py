'''
Projeto Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a 
velocidade e com base nessa velocidade diga se ela tomou um multa leve, grave ou gravissima. Levanddo em consideração que se a pessoa estiver abaixo da velocidade máxima 
seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja eentre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", 
e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravissima"

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)
1. Quais são os dados de entrada necessários?
velocidade maxima, velocidade recebida
2. O que devo fazer com estes dados?
comparalos e com base nisso diga se ela tomou um multa leve, grave ou gravissima.
3. Quais são as restrições deste problema?
faixas de km
4. Qual é o resultado esperado?
se a pessoa estiver abaixo da velocidade máxima 
seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja eentre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", 
e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravissima"
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
'''
''''
vel_max = 80
vel_user = int(input('Qual sua velocidade no momento do radar? '))

if vel_user > vel_max:
    if vel_user in range(81, 91):
        print('levou multa leve')
    elif vel_user in range(91, 101):
        print('levou multa grave')
    else:
        print('levou multa gravissima')
else:
    print('não houve multa')

'''

vel_max = 80
vel_user = int(input('Qual sua velocidade no momento do radar? '))

if vel_user <= vel_max:
    print('não houve multa')
elif vel_user <= vel_max + 10 and vel_user > vel_max:
        print('levou multa leve')
elif vel_user >= vel_max + 11 and vel_user <= vel_max+20:
        print('levou multa grave')
elif vel_user > vel_max + 20:
        print('levou multa gravissima')
