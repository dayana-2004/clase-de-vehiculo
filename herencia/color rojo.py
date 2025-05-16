class Rectangulo:
    def __init__(self, ancho, alto, color="Rojo"):
        self.ancho = ancho
        self.alto = alto
        self.color = color

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f"Rectángulo de {self.ancho}x{self.alto}, Color: {self.color}, Área: {self.area()}"

# Ejemplo de uso
r1 = Rectangulo(6, 3, "Rojo")
print(r1)
