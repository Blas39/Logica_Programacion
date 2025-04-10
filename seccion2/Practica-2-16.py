monto_total:float = 0

compra = float(input("Ingrese un monto "))

while compra != 0:
    if(compra < 0) :
        print("Monto no valido")
        compra = float(input("Ingrese un monto "))
    else:
        monto_total += compra
        compra = float(input("Ingrese un monto "))

if(monto_total > 1000) :
    monto_total -= (monto_total * (10/100))

print("Monto total a pagar: ", monto_total)