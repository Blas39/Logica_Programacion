primer_nombre = input("Ingrese el primer nombre ")
segundo_nombre = input("Ingrese el segundo nombre ")

condicion:bool = (primer_nombre[0] == segundo_nombre[0]) or (primer_nombre[len(primer_nombre) - 1] == segundo_nombre[len(segundo_nombre) - 1])
print(condicion)