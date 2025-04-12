def esPar(num):
    return (num % 2 == 0)



sum_par = 0
sum_impar = 0

for i in range(10):
    numero = int(input("Ingresa un numero: "))
    if(esPar(numero)):
        sum_par+=numero
    else:
        sum_impar+=numero

print("Suma de los pares:", sum_par)
print("Suma de los impares:", sum_impar)
    