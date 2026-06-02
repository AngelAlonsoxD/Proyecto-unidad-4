num1 = int(float(input("Ingresa primer numero: ")))
num2 = int(float(input("Ingresa segundo numero: ")))
numero = num1 + num2
if numero > 0:
    print("El numero es positivo: ", numero)
elif numero < 0:
    print("El numero es negativo: ", numero)
else:
    print("El numero es cero")