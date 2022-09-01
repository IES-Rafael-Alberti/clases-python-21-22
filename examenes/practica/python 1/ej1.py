import random

def filtra_ejercicios(ejercicios, minutos):
	resultado = list()
	for ejercicio in ejercicios:
		if ejercicio["duracion"] <= minutos:
			resultado.append(ejercicio)
	return resultado

def duracion_ejercicios(ejercicios):
	resultado = 0
	for ejercicio in ejercicios:
		resultado += ejercicio["duracion"]
	return resultado

# ejercicio.get("duracion") == ejercicio["duracion"]

def entrenamiento(ejercicios, minutos):
	resultado = []
	resto = ejercicios[:]
	while duracion_ejercicios(resultado) != minutos:
		nuevo_ejercicio = random.choice(filtra_ejercicios(resto, minutos - duracion_ejercicios(resultado)))
		resto.remove(nuevo_ejercicio)
		resultado.append(nuevo_ejercicio)
	random.shuffle(resultado)
	return resultado
		
