stringcompleto = input("Ingresa una cadea de caracteres")
count_num:int = 0
count_mult4:int = 0
count_letra:int = 0
count_simbol:int = 0

for i in stringcompleto:
    if(i.isnumeric()):
        count_num +=1
        if(float(i) % 4 == 0): count_mult4 +=1
    elif(i.isalpha()):
        count_letra += 1
    else:
        count_simbol += 1

print("Cantidad de Letras:", count_letra)
print("Cantidad de Numeros:", count_num)
print("Cantidad de simbolos:", count_simbol)
print("Cantidad de multiplos de 4:", count_mult4)
