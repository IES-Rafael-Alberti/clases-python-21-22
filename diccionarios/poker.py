mano1 = "2D 2P 3T 3C AP"
mano2 = "5D 5P 7T 5C AC"

cartas = mano1.split()

numeros = {} #dict()
palos = {}

for carta in cartas:
	if carta[0] in numeros:
		numeros[carta[0]] += carta[1]
	else:
		numeros[carta[0]] = carta[1]
	if carta[1] in palos:
		palos[carta[1]] += carta[0]
	else:
		palos[carta[1]] = carta[0]

print(numeros)
print(palos)
	

