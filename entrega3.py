from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


class Triangulo(Figura):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        # Fórmula de Herón
        s = self.perimetro() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

c = Circulo(5)
r = Rectangulo(4, 6)
t = Triangulo(3, 4, 5)

print("Círculo:", c.area(), c.perimetro())
print("Rectángulo:", r.area(), r.perimetro())
print("Triángulo:", t.area(), t.perimetro())