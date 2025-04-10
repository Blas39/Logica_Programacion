numero_1 = int(input("Ingrese primer numero "))
numero_2 = int(input("Ingrese segundo numero "))
numero_3 = int(input("Ingrese tercer numero "))

if(numero_1 < numero_2):
    if(numero_1 < numero_3):
        print(numero_1, " menor")
    else : 
        print(numero_3, " menor")
else : 
    if(numero_2 < numero_3):
        print(numero_2, " menor")
    else :
        print(numero_3, " menor")