total_alumnos:int = 0
total_aprobados:int = 0
total_coapro:float = 0

analizar = input("¿Analizar calificaciones? ‘S’ para ‘sí’ ").lower()


while analizar == "s":
    calificacion = int(input("Ingrese calificacion de alumno "))
    if(calificacion > 4): 
        total_aprobados+=1
        total_coapro+=calificacion
    total_alumnos+=1
    analizar = input("¿Analizar calificaciones? ‘S’ para ‘sí’ ").lower()


prom_aprobados = total_coapro/total_aprobados
print("Promedio de aprobados", prom_aprobados)
print("Porcentaje de aprobados", (total_aprobados*100)/total_alumnos)