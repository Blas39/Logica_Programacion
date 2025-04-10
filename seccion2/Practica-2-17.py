numero_mayor:int = 0

numero = int(input("Ingrese un numero "))

while numero != 0:
    if(numero > numero_mayor): numero_mayor = numero
    numero = int(input("Ingrese un numero "))

print(numero_mayor)