edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 100:
    print("Edad inválida. Por favor ingrese un valor positivo.")
elif edad <= 12:
    print("Tarifa de entrada: $50")
elif edad <= 17:
    print("Tarifa de entrada: $80")
else:
    print("Tarifa de entrada: $120")