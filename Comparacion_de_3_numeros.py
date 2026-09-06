A = float(input("Ingrese el primer número: "))
B = float(input("Ingrese el segundo número: "))
C = float(input("Ingrese el tercer número: "))

if A > B and A > C:
    print(f"El número mayor es: {A}")
elif B > A and B > C:
    print(f"El número mayor es: {B}")
else:
    print(f"El número mayor es: {C}")