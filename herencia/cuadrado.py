import turtle

def dibujar_cuadrado(lado):
    ventana = turtle.Screen()
    ventana.title("Dibujo de un Cuadrado")

    cuadrado = turtle.Turtle()
    cuadrado.speed(3)

    for _ in range(4):
        cuadrado.forward(lado)
        cuadrado.right(90)

    ventana.mainloop()

dibujar_cuadrado(100)