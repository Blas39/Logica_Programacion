caracter = input("Ingresa un solo caracter ")
string_completo:str = ""
a_count:int = 0

while len(caracter) == 1 and caracter != "0":
    string_completo+=caracter
    if(caracter == "a"): a_count+=1
    caracter = input("Ingresa un solo caracter")

print(string_completo)
print("Porcentaje de letra a", (a_count*100)/len(string_completo))



