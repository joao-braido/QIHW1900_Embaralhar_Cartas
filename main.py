import random
naipes = ['Ouro', 'Copas', 'Espadas', 'Paus']
numeros = ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
cartas = [] 

for i in range(4): #for para naipes
  for u in range(13): #for para numeros
     cartas.append(str(numeros[u])+ " de "+naipes[i])

quantidade = int(input("Digite a quantidade de cartas"))

random.shuffle(cartas)
for i in range(quantidade):
  print(cartas[i])
