import turtle
import random


#set up the screen
ws = turtle.Screen()
ws.bgcolor("powder blue")

#default shape
current_shape = "pentagon"  


#create the turtle
will = turtle.Turtle()
will.speed(0)
will.shape("turtle")
will.pensize(5)

#reposition turtle
will.penup()
will.left(108)
will.backward(100)
will.pendown()


def change(*args):
    #clear previous drawing
    will.clear()
    
    #generate random colors
    fill_color = (random.random(), random.random(), random.random())
    pen_color = (random.random(), random.random(), random.random())
    
    #set colors 
    will.fillcolor(fill_color)
    will.pencolor(pen_color)

    will.begin_fill()
    
    #draw pentagon
    if current_shape == "pentagon":
            for _ in range(5):
                will.forward(200)
                will.right(72)
                
    #draw circle
    elif current_shape == "circle":
            will.circle(100)
            

    will.end_fill()

#change shape
def toggle_shape():
    global current_shape
    current_shape = "circle" if current_shape == "pentagon" else "pentagon"
    
ws.onscreenclick(change)

#bind the key press event to the toggle_shape function
ws.listen()
ws.onkey(toggle_shape, "space")  # Change shape on spacebar press

turtle.done()