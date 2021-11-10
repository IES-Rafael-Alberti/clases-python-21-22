class Mamifero:
	def __init__(self, nombre, denominacion, habitat, peso_medio):
		self.nombre = nombre
		self.denominacion = denominacion
		self.habitat = habitat
		self.peso_medio = peso_medio

	def __str__(self):
		return self.nombre +" es un/a " + self.denominacion + ", vive en " + self.habitat + " y suele pesar " + self.peso_medio

class Mascota:
	def es_buena(self):
		return True

class Morsa(Mamifero, Mascota):
	def __init__(self, nombre):
		Mamifero.__init__(self, nombre, "Morsa", "Casquete polar ártico", "1T")

if __name__ == "__main__":
	m1 = Morsa("David")
	print(m1)
	print(m1.es_buena())
