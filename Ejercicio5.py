calificacion = int(input("Ingrese su calificacion: "))
if calificacion == 10 or calificacion == 9:
    print("Excelente")
elif calificacion == 8 or calificacion == 7:
    print ("Aprobado")
elif calificacion == 6:
    print("suficiente")
elif calificacion < 6:
    print("Reprobado")
else:
    print("Calificacion noa valida")
