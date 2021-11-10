while True:
    try:
            n = int(input("numero: "))
            print(f" correcto, {n} es un número!!! ")
            break # opcion 1
    except ValueError:
            print("No es un número")

while True:
    try:
            n = int(input("numero: "))
            print(f" correcto, {n} es un número!!! ")
    except ValueError:
            print("No es un número")
            continue # opcion 2
    break

print("El programa se termina...")

###### bucle for con continue
for a in (3,4,-5,6):
    if a < 0:
        continue
    print(a)