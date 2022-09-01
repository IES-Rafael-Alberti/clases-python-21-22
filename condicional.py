nombres_tradicionales = ['José', 'María']
a = input("Nombre: ")
# tradicional
if a in nombres_tradicionales:
    tradicional = True
else:
    tradicional = False

# alternativa
tradicional = True if a in nombres_tradicionales else False
# Java, C, php, etc...
tradicional = condicion ? True : False;