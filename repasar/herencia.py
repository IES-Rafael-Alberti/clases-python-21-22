class Base:
	def __init__(self, atributo1):
		self.atributo1 = atributo1

class HijoA(Base):
	def __init__(self):
		Base.__init__(self, "HijoA")

class HijoB(Base):
	def __init__(self):
		super(HijoB, self).__init__("HijoB")

