class contador:
    def __init__(self):
        self._valor = 0
    def incrementar(self):
        self._valor += 1
    def decrementar(self):
        self._valor -= 1
    def valor(self):
        return self._valor

c = contador()
c.incrementar()
c.incrementar()
c.decrementar()
print ("valor actual:", c.valor())