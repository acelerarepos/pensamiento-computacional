import turtle

def cuadrado(lado):
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    
    
miT = turtle.Turtle()
cuadrado(25)
miT.left(90)

cuadrado(50, "El segundo es mayor")
miT.left(90)

cuadrado(75, "ya casi acabo")
miT.left(90)

cuadrado(100, "terminé")
miT.left(90)





