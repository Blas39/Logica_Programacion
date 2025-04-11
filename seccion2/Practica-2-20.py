numero:int = int(input("Ingrese un numero "))
sum_total:float = 0

while (numero > 0):
    sum_total+= (numero%10)
    numero = int(numero/10)

print("Suma de los dígitos", sum_total)

