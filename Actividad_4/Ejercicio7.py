monto_total = float(input("Ingrese el monto a pagar: "))
satisfaccion = input("El servicio fue bueno o malo?")
if satisfaccion == "bueno":
    propina = monto_total * 0.15
elif satisfaccion == "mala":
    propinam = monto_total * 0.05
else:
    print("El servicio no fue bueno")
total_pagar = monto_total + propina
print("El total es: ", total_pagar)

