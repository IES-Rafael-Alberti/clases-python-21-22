class Cliente:
	def __init__(self, email, facturas=None):
		self.email = email
		if facturas==None:
			self.facturas = []
		else:
			self.facturas = facturas

	def __str__(self):
		resultado = ""
		resultado += self.email + "\nLista de facturas:\n"
		for f in self.facturas:
			resultado += str(f) + "\n"	
		return resultado

	def alta_factura(self, factura):
		self.facturas.append(factura)

	def lista_facturas(self):
		return self.facturas

if __name__ == "__main__":
	c1 = Cliente("jo")
	c2 = Cliente("ja")
	c1.alta_factura("122")
	print(c1)
	print(c2)