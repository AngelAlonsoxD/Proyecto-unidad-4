class animal:
    def hablar(self):
        return "El animal hace un sonido"

class Perro (animal):
    def hablar(self):
        return "Guau "

class Gato (animal):
    def hablar(self):
        return "Miau"


perro = Perro()
gato = Gato()

print(perro.hablar())
print(gato.hablar())