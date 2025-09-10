# Programa que convierta una calificación numérica en letra (ej. 90–100 → A, 80–89 → B, etc.)

calificacion =  int(input("Ingrese su calificación: "))

if 90 <= calificacion <= 100:
    print("A")  
elif 80 <= calificacion <= 89:
    print("B")
elif 60 <= calificacion <= 79:
    print("C")
else:
    print("D/F")