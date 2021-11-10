import random

print(random.randint(1, 10))
alumnos = [ "Lorena",
            "Gonzalo",
            "Judith",
            "Rafa",
            "Alejandro",
            "Raul",
            "Hugo",
            "Víctor",
            "David",
            "JA",
            "Jairo",
            "Juan",
            "Carolina",
            "JJ",
            "Javier"]

random.shuffle(alumnos)
print("Orden: " + repr(alumnos))