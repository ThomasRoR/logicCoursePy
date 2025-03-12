#Crie um programa que recebe um número e imprime o seu fatorial.

# Método 5Q's para montar um algoritimo:

#Analise criticamente o problema e descubra:

#1. Quais são os dados de entrada necessários?
#   numero
#2. O que devo fazer com estes dados?
#  eu devo calcular o fatorial do número que for passado para o meu programa e o exibir na tela.
#3. Quais são as restrições deste problema?
#   deve ser inteiro e positivo
#4. Qual é o resultado esperado?
#   o resultado do fatorial
#5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?

numero = int(input('digite um num:'))
if numero <= 0:
    print('não é possivel fazer co meste numero')
else:
    fatorial = 1
    for num in range(1, numero +1):
        fatorial = fatorial * num
    print(fatorial)\
    
