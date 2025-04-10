vocales = ["a", "e", "i", "o", "u"]
num_vocales:int = 0

texto = input("Ingrese un texto ")

for i in texto:
    if(i.lower() in vocales): num_vocales += 1

print("Vocales:", num_vocales)