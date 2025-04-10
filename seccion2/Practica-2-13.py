numeros = [0, 0, 0, 0, 0 ,0]

sum_neg:int = 0
prom_pos:int = 0
cont_pos:int = 0

numeros[0] = int(input("Ingrese un numero "))
numeros[1] = int(input("Ingrese un numero "))
numeros[2] = int(input("Ingrese un numero "))
numeros[3] = int(input("Ingrese un numero "))
numeros[4] = int(input("Ingrese un numero "))
numeros[5] = int(input("Ingrese un numero "))

for i in numeros : 
    if(i > 0):
        cont_pos+=1
        prom_pos+=i
    else:
        sum_neg+=i

if(cont_pos != 0): prom_pos = prom_pos/cont_pos

print("Sumatoria de los negativos:", sum_neg)
print("Promedio de los positivos:", prom_pos)
