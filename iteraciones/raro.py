def cambia_lista(lista = None):
    if lista is None:
        lista = []
    lista.append(5)
    return lista

if __name__ == "__main__":
    lista_nueva = cambia_lista()
    otra_lista = cambia_lista()
    print(lista_nueva)
    print(otra_lista)