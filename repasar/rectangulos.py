from puntos import Punto

class Rectangulo():
    def __init__(self, pi, pf):
        #if type(pi) != type(Punto(0,0)) or type(pf) != type(Punto(0,0)):
        #if not type(pi) is Punto or not type(pf) is Punto:
        if not isinstance(pi, Punto) or not isinstance(pf, Punto):
            raise ValueError("Los valores deben ser de la clase Punto")
        self.pi = pi
        self.pf = pf

    def __str__(self):
        return "Rectángulo desde "+str(self.pi)+" hasta "+str(self.pf)
    
    def area(self):
        return abs(self.pi.x-self.pf.x) * abs(self.pi.y-self.pf.y)

    
if __name__ == "__main__":
    p1 = 4
    p2 = Punto(6,7)
    try:
        mirecto = Rectangulo(p1,p2)
        print("No se controlan los tipos")
    except ValueError:
        print("Correcto")
    p1 = Punto(3,5)
    mirecto = Rectangulo(p1,p2)
    print(mirecto)