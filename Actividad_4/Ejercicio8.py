usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese la clave: ")
if usuario == "admin" and contraseña == "1234admin":
    print("Acceso permitido")
else:
    print("Acceso denegado")