#Calificacion cualitativa
#solicita una calificacion numerica entre 0 y 100 y muestre si es
#Reprobado (menos de 70), Regular (70-79), Bueno (80-89), Muy bueno (90-95), Excelente (96-100)

calificacion = int(input("Ingrese su calificación: "))

if(calificacion >= 0 and calificacion < 70):
    print("Usted ha reprobado")
elif(calificacion >= 70 and calificacion <=79):
    print("Su nota es regular")
elif(calificacion >= 80 and calificacion <= 89):
    print("Su nota es buena.")
elif(calificacion >=90 and calificacion <= 95):
    print("Su nota es Muy buena.")
elif(calificacion >= 96 and calificacion <=100):
    print("Su nota es Excelente.")
else:
    print("La calificacion que ha introducida no es valida.")
