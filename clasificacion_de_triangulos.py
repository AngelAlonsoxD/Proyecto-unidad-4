lado1 = int(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = int(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = int(input("Ingrese la longitud del tercer lado del triángulo: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")