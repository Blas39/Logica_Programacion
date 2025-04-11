string_mult3 = ""
string_cont0 = ""

numero = input("Ingresa un numero ")
while (int(numero) < 0 or int(numero) % 10 != 0):
    if(len(numero) % 3 == 0): string_mult3 += numero + "-"
    if("0" in numero): string_cont0 += numero + "-"
    numero = input("Ingresa un numero ")

print("Números cuya cantidad de dígitos es múltiplo de 3:", string_mult3)
print("Números que contienen el 0:", string_cont0)