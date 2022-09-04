import json
import yaml

ld1 = json.load(open('ejemplo.json'))
ld2 = yaml.load(open('ejemplo.yaml'))

for alumno in ld1:
    print(alumno.get("nombre"))

for alumno in ld2:
    print(f"Nombre: {alumno.get('nombre')} Edad: {alumno.get('edad')}")


datos = [{"card": "Strike", "n": 3},
         {"card": "Defense", "n": 3},
        ]
manf = open("basic_deck.json", "w")
json.dump(datos, manf)
manf.close()
