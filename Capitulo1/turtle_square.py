import turtle

window = turtle.Screen()
tortuga = turtle.Turtle()

contador = 0

while (contador < 4):
    tortuga.forward(100)
    tortuga.right(90)
    contador+=1

window.mainloop()