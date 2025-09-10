# Programa que calcule el área de un triángulo, cuadrado o círculo según lo que elija el usuario.

area = input("¿Qué area deseas calcular? (triangulo, cuadrado, circulo): ").strip().lower()

if area == "triangulo": 
    base = int(input("Ingrese la base del triangulo: "))    
    altura = int(input("Ingrese la altura del triangulo: "))
    resultado = (base * altura) / 2
elif area == "cuadrado":
    lado = int(input("Ingrese el tamaño del lado del cuadrado: "))
    resultado = lado * lado
else:
    radio = int(input("Ingrese el radio del circulo: "))
    pi = 3.14159
    resultado = pi * pow(radio, 2)

print("El area de la figura es:", resultado)