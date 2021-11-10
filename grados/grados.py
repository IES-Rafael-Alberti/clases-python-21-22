def grados_fahrenheit(grados_centigrados):
    """Convierte grados centígrados en grados fahrenheit
    """
    return (grados_centigrados * 9 / 5) + 32

if __name__ == "__main__":
    try:
        grados = float(input("Grados centígrados: "))
        print("Grados Fahrenheit:", grados_fahrenheit(grados))
    except ValueError:
        print("No es un número")