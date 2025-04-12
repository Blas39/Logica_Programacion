frase = input("Ingrese frase a invertir ")
frase_inv:str = ""

for i in range(len(frase)): 
    frase_inv += frase[i + ((len(frase) - 1) - (i*2))]


texto = input("Ingrese una Frase").tolower()

print(frase_inv)

