def esinicial9(num):
    while (num > 10):
        num = num//10 #dividir hasta que quede solo el primer digito
    return (num == 9)

count_2divisores:int = 0 #cantidad de numero que tengan solo 2 divisores
numero = int(input("Ingresa un numero "))
while not esinicial9(numero):
    divi:int = 0 #cantidad de divisores

    for i in range(1, numero + 1) :
        if(numero % i == 0) : divi +=1

    if(divi == 2): count_2divisores +=1

    numero = int(input("Ingresa un numero "))

print("Numeros con 2 Divisores:", count_2divisores)
