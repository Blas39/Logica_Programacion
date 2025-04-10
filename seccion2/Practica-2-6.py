year = int(input("Ingrese año "))

if(year % 4 == 0):
    if(year % 100 != 0 or year % 400 == 0):
        print("Bisiesto")
    else:
        print("No bisiesto")
else: 
    print("No bisiesto")
