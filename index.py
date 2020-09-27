def Agregar_Producto():
    print("Agregar producto")
    archivo = open("prueba.txt", "w")
    producto = input("ingrese nombre del producto: \n")
    archivo.write("producto =" + " " + producto)
    archivo.write("\n")
    precio = float(input("ingrese precio del producto: \n"))
    archivo.write('precio = % s' % precio)
    archivo.write("\n")
    cantidad = int(input("ingrese la cantidad del producto que lleva: \n"))
    archivo.write('cantidad = % s' % cantidad)
    archivo.write("\n")
    
    archivo.close()

    print("producto agregado")
    print(" ")
    print("1. Agregar otro producto?")
    print("3. imprimir detalle de los productos agregados")
    print("2. Menú anterior")
    opcion2 = input("ingrese opcion: ")
    if opcion2 == "1":
        Agregar_Producto()
    elif opcion2 == "2":
        menu()
    elif opcion2 == "3":
        archivo = open("prueba.txt")

        print(archivo.read())
        archivo.close()
    menu()

def menu():
    
    print("productos a facturar")
    print(" ")
    print("1. Agregar Datos personales")
    print("0. Agregar producto")
    print("2. Imprimir Factura")

    opcion = input("ingrese una opción: ")

    if opcion == "0":
        Agregar_Producto()
    elif opcion == "1":
            print("Ingresa tus datos personales")
            print(" ")
            print("1. datos personales")
            print("2. menu anterior")
            opcion1 = input("ingresa opcion: ")
            if opcion1 == "1":
                cliente = input("Nombre: ")
                nit = input("NIT: ")
                direc = input("Direccion: ")
                fecha = input("Fecha: ")
                serie = input("Serie: ")
                factura = int(input("Número de factura: "))
                menu()
            if opcion == "2":
                menu()
    if opcion == "2":
        print(serie, + factura)
        print(fecha)
        print(cliente)
        print(direc)
        print(nit)

menu()
