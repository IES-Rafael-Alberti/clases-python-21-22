class Punto():
    """FORBIDDEN!!!
    x = 0
    y = 0"""

    def __str__(self):
        return f"x: {self.x} , y: {self.y}"  

    def __init__(self, x, y):
        #if type(x) != type(0) or type(y) != type(0):
        #if not type(x) is int or not type(y) is int:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Las coordenadas solo pueden ser valores int")
        self.x = x
        self.y = y 
    


if __name__ == "__main__":
    try:
        Punto("orto","nadal")
        print("Esto debe dar error")
    except ValueError:
        print("Controla el tipo de los datos")
    p = Punto(3,4)
    print(p)

