def my_generator(seed):
    print("Inicio")
    while seed < 50:
        yield seed
        seed += 2
    print("Fin")


class My_with:
    def __enter__(self):
        print("Hola")
    def __exit__(self, *args, **kargs):
        print("Adios")


with My_with() as mg:
    for number in my_generator(4):
        print(number)


