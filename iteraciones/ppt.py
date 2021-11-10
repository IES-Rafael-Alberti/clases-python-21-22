def jugada_ppt(j1, j2):
    reglas = { "Piedra" : "Papel",
               "Papel" : "Tijera",
               "Tijera" : "Piedra" }
    return (reglas[j1] == j2) * -1 + (reglas[j2] == j1) * 1

def partida_ppt(l1, l2):
    return sum([ jugada_ppt(j1, j2)
                 for j1, j2 in list(zip(l1, l2)) ])

if __name__ == "__main__":
    textos = {"P": "Piedra", "A":"Papel", "T":"Tijera"}
    print("Iniciales Piedra/Papel/Tijera:")
    for clave, valor in textos.items():
        print(f"Inicial: {clave} -> {valor}")
    jugada1 = input("Carga jugada con iniciales J1: ")
    jugada2 = input("Carga jugada con iniciales J2: ")
    l1 = [ textos[inicial] for inicial in jugada1 ]
    l2 = [ textos[inicial] for inicial in jugada2 ]
    resultado = partida_ppt(l1, l2)
    print("Ha ganado J1" if resultado>0 else ("Ha ganado J2" if resultado<0 else "Empate..."))
    # Java:
    # resultado>0 ? "ha ganado J1" : (resultado<0 ? "J2" : "empate")

    # if resultado>0:
    #     print("Ha ganado J1")
    # elif resultado<0:
    #     print("Ha ganado J2")
    # else:
    #     print("Empate...")

