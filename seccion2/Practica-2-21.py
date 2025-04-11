cant_mult3:int = 0
numero = int(input("Ingrese un numero entero positivo (-1 para finaliizar) "))

while numero != -1:
    if(numero % 3 == 0): cant_mult3+=1

    num:int = numero
    cant_par:int = 0
    cant_impar:int = 0

    while num > 0:
        digito:int = num%10
        num = int(num/10)
        if(digito % 2 == 0):
            cant_par +=1
        else:
            cant_impar +=1
    
    print("Digitos pares:", cant_par)
    print("Digitos impares:", cant_impar)
    numero = int(input("Ingrese un numero entero positivo (-1 para finaliizar) "))

print("Multiplos de 3:",cant_mult3)

