class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monto a depositar debe ser positivo")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor que 0")
        elif monto > self.__saldo:
            print("Fondos insuficientes")
        else:
            self.__saldo -= monto

    def saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(1000)

cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(2000)  # error por fondos insuficientes

print("Saldo actual:", cuenta.saldo())