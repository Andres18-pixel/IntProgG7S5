rango_inicial = int(input("Escribe el inicio del rango: "))
rango_final = int(input("Escribe el final del rango: "))

if(rango_inicial < rango_final):
    numero = int(input("Dime un numero: "))
    if(numero >=rango_inicial and numero <= rango_final):
        print("El número está dentro del rango.")
    else:
        print("El número está fuera del rango.")
else:
    print("El rango inicial no puede ser mayor que el rango final")
    