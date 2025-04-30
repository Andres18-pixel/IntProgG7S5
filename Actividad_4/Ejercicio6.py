calificacion = float(input("Ingrese la calificacion del estudiante (0-100): "))
if 0 <= calificacion <= 100:
    if calificacion >= 70:
        print("Aprobado")
    else:
        print("Reprobado")