from ej1 import *
from ejercicios import ejercicios

def test_filtro():
	assert len(filtra_ejercicios(ejercicios, 30)) == 33
	assert len(filtra_ejercicios(ejercicios, 20)) == 30
	assert len(filtra_ejercicios(ejercicios, 10)) == 20

def test_duracion():
	assert duracion_ejercicios(ejercicios) == 490
	assert duracion_ejercicios(filtra_ejercicios(ejercicios, 20)) == 400
	assert duracion_ejercicios(filtra_ejercicios(ejercicios, 10)) == 200

def test_entrenamiento():
	assert duracion_ejercicios(entrenamiento(ejercicios, 50)) == 50
	assert duracion_ejercicios(entrenamiento(ejercicios, 10)) == 10
	assert duracion_ejercicios(entrenamiento(ejercicios, 490)) == 490


