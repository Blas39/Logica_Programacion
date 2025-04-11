count_lineas:int = 0
count_num:int = 0

cadena = input("ingrese una cadena: ")

while ("*" not in cadena):
    for i in cadena: 
        if(i.isnumeric()): count_num +=1

    if(cadena == "/") :
        count_lineas += 1
        print("Cantidad de digitos en linea:", count_num)
        count_num = 0

    cadena = input("ingrese una cadena: ")

print("Cantidad de lineas:", count_lineas)
