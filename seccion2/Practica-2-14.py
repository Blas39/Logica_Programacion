frase = input("Ingrese una frase ")
carac = input("Seleccione un caracter ")

for i in frase:
    if(i == carac) : frase = frase.replace(i, "*")

print(frase)