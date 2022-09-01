from ejercicios import ejercicios
from ej1 import entrenamiento, filtra_ejercicios

def imprime_ejercicio(ejercicio):
    print(f"{ejercicio.get('denominacion')} ({ejercicio.get('duracion')} mins)")
    print(ejercicio.get("descripcion"))
    print("Estrategia:")
    for estrategia in ejercicio.get("estrategia"):
        print(f"- {estrategia}")
    print()

def imprime_ejercicios(lista):
    for ejercicio in lista:
        imprime_ejercicio(ejercicio)

if __name__ == "__main__":
	while True:
		orden = input(":")
		if orden == "fin":
			break
		elif orden == "listar":
			imprime_ejercicios(ejercicios)
		elif orden.startswith("entrenamiento"):
			try:
				duracion = int(orden.split()[1])
				if duracion <= 0 or duracion%10 != 0:
					raise ValueError
				imprime_ejercicios(entrenamiento(ejercicios, duracion))
			except ValueError:
				print("Debe ser un número positivo múltiplo de 10")
			except IndexError:
				print("Debes indicar una duración") 
		elif orden.startswith("consulta"):
			try:
				duracion = int(orden.split()[1])
				if duracion <= 0 or duracion%10 != 0:
					raise ValueError
				imprime_ejercicios(filtra_ejercicios(ejercicios, duracion))
			except ValueError:
				print("Debe ser un número positivo múltiplo de 10")
			except IndexError:
				print("Debes indicar una duración") 
			
