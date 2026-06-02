num1 = int(float(input("Ingrese el primer numero: ")))
num2 = int(float(input("Ingrese el segundo numero: ")))
opcion = int(input("Elige una opcion: "))
match opcion:
    case 1:
        resultado = num1 + num2
        print("Suma: ", resultado)
    case 2:
        resultado = num1 - num2
        print("Resta: ", resultado)
    case 3:
        resultado = num1 * num2
        print ("Multiplicacion: ", resultado)
    case 4: 
        resultado = num1 / num2
        print ("Division: ", resultado)
    case 5:
        resultado = num1 ** num2
        print ("Potenciacion: ", resultado) 
    case 6:
        print("Salir")
    case _:
        print("Opcion no valida ")