class rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

rect = rectangulo(5,3)
print ("Area:", rect.area())
print("perimetro:", rect.perimetro()) 