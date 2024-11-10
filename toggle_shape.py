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


def change(*args): # onscreenclick() function in Turtle automatically passes the mouse click's x and y coordinates to the change(), making *args necessary to capture these values even if they aren’t used
    
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
    global current_shape # global keyword to modify the variable current_shape that was defined outside of this function, making it persist across multiple function calls
    current_shape = "circle" if current_shape == "pentagon" else "pentagon" # ternary operator to change the value of current_shape based on its current value
    
ws.onscreenclick(change)

ws.listen() #tells the program to start listening for user inputs, such as keyboard presses or mouse clicks
ws.onkey(toggle_shape, "space")  # binds the spacebar key to the toggle_shape function

# tells the turtle graphics system that the program is finished, without it the window may close immediately after running the program
turtle.done() 
