frase = input("Ingrese frase a invertir ")
frase_inv:str = ""

for i in range(len(frase)): 
    frase_inv += frase[i + ((len(frase) - 1) - (i*2))]

print(frase_inv)

