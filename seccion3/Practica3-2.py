def sumatoriaDigitos(num):
    sum_total:float = 0
    
    while (num> 0):
        sum_total+= (num%10)
        num = int(num/10)

    return sum_total


numero = int(input("Ingrese numero: "))

while numero != 100:
    print("Suma de los digitos:", sumatoriaDigitos(numero))
    numero = int(input("Ingrese numero: "))