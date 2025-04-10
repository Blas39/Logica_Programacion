usr_correcto:str = "Gwenevere"
pass_correcto:str = "excalibur"

usuario = input("Ingrese nombre de usuario ")
password = input("Ingrese contraseña ")

if(usuario != usr_correcto or password != pass_correcto) :
    print("Acceso Denegado")
    exit()
else :
    print("Bienvenido")



