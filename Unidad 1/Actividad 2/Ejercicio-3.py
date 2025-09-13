# Crear un menú con opciones (ej. “1. Suma, 2. Resta, 3. Salir”) usando while.

while True:
    print("Ingrese su operacion deseada")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. Salir")
    operacion = int(input("> "))

    if operacion == 1:
        print("Seleccionado la opcion de suma")
    elif operacion == 2:
        print("Seleccionado la opcion de resta")
    elif operacion == 3:
        print("Seleccionado la opcion de multiplicacion")
    elif operacion == 4:
        print("Seleccionada la opcion de division")
    elif operacion == 5:
        print("Gracias por probar")
        break
    else:
        print("Opcion invalida")

    opcion = input("¿Deseas seleccionar otra operacion? si/no -> ").strip().lower()
    if opcion != "si":
        print("Gracias por probar")
        break
