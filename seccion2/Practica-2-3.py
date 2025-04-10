letra = input("Ingrese una letra ")
vocales = ["a", "e", "i", "o", "u"]


if(len(letra) > 1) : 
    print("No se puede procesar mas de una letra") 
    exit()
else:
    if(letra.lower() in vocales) :
        print("Es una vocal")
    else: 
        print("No es una vocal")