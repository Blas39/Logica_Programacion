def sumatoriaDigitos(num):
    sum_total:float = 0
    
    while (num> 0):
        sum_total+= (num%10)
        num = int(num/10)

    return sum_total

def esPar(num):
    return (num % 2 == 0)

count_impar:int = 0
numero = int(input("Ingrese un numero"))

while (sumatoriaDigitos(numero) < 1000) and (sumatoriaDigitos(numero) % 5 != 0):
    if not esPar(numero): count_impar +=1
    numero = int(input("Ingrese un numero"))

print("Cantidad de impares:", count_impar)