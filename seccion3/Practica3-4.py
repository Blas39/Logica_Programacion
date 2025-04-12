def esPalindromo(texto:str):
    texto_inv:str = ""
    
    for i in range(len(texto)): 
        texto_inv += texto[i + ((len(texto) - 1) - (i*2))]

    return (texto == texto_inv)

count_pali:int = 0
texto = input("Ingrese una Frase ").lower()

while texto != "fin":
    if esPalindromo(texto): count_pali += 1
    texto = input("Ingrese una Frase ").lower()

print("Cantidad de palíndromos:", count_pali)