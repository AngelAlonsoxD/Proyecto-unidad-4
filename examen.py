#1
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo  # accesible directamente
        self.__nip = 1234     # accesible directamente

    def depositar(self, monto):
        self.saldo += monto
#2
from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

    @abstractmethod
    def generar_recibo(self):
        pass
class PagoTarjeta(MetodoPago):
    def __init__(self, numero_tarjeta, titular):
        self.numero_tarjeta = numero_tarjeta
        self.titular = titular
        self.transaccion_exitosa = False

    def procesar_pago(self, monto):
        # Lógica simulada: validación básica
        if len(str(self.numero_tarjeta)) == 16:
            print(f"Procesando pago de ${monto} con tarjeta de {self.titular}...")
            self.transaccion_exitosa = True
        else:
            print("Número de tarjeta inválido.")
            self.transaccion_exitosa = False

    def generar_recibo(self):
        if self.transaccion_exitosa:
            return f"Recibo: Pago con tarjeta de {self.titular} aprobado."
        else:
            return "Recibo: Pago fallido."
