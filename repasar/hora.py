class Hora:
    def __init__(self,horas,minutos,segundos):
        # Control de corrección de los parámetros
        ## TODO: Control del tipo de datos (Thanks to Christhian)
        if not isinstance(horas, int) or not isinstance(minutos, int) or not isinstance(segundos, int):
            raise ValueError("Solo valores int")
        ## TODO: Control de corrección valores
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def __str__(self):
        return f"{self.horas}:{self.minutos}:{self.segundos}"



if __name__ == "__main__":
    hora = Hora(2,3,23)
    print(hora)

