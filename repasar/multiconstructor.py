class Prueba:
    def __init__(self, **argumentos):
        print(argumentos)
    
if __name__ == "__main__":
    p1 = Prueba()
    p2 = Prueba(a=3,b=5,c=6)
    p3 = Prueba(litros="jh")
    p4 = Prueba(y=7.6, p1=p2, p2=p1)
