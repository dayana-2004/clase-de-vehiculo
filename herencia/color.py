import turtle


def dibujar_rectangulo_rojo(ancho, alto):
    ventana = turtle.Screen()
    ventana.title("Dibujo de un Rectángulo Rojo")

    rectangulo = turtle.Turtle()
    rectangulo.speed(3)
    rectangulo.color("red")
    rectangulo.begin_fill()

    for _ in range(2):
        rectangulo.forward(ancho)
        rectangulo.right(90)
        rectangulo.forward(alto)
        rectangulo.right(90)

    rectangulo.end_fill()

    ventana.mainloop()


dibujar_rectangulo_rojo(150, 100)