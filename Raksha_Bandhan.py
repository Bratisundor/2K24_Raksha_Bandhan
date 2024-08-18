import math
import turtle
import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Initialize Turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.color("black")
tina.speed(0)

# Positioning function
def pos(x, y):
    tina.penup()
    tina.goto(x, y)
    tina.pendown()

# Function to draw the Rakhi
def draw_rakhi():
    # Start playing the background music
    pygame.mixer.music.load("Raksha_Bandhan_2K24.mp3")
    pygame.mixer.music.play()

    # Draw a filled circle (Base of Rakhi)
    tina.color("light green")
    tina.begin_fill()
    pos(0, -250)
    tina.circle(250)
    tina.end_fill()

    # Draw seeds in a spiral pattern (Rakhi's decorative part)
    def draw(t, numseeds, angle, cspread):
        t.fillcolor("Orange")
        phi = angle * (math.pi / 180.0)

        for i in range(numseeds):
            r = cspread * math.sqrt(i)
            theta = i * phi
            x = r * math.cos(theta)
            y = r * math.sin(theta)

            t.penup()
            t.goto(x, y)
            t.setheading(i * angle)
            
            if i < numseeds:
                t.stamp()

    draw(tina, 500, 18.7, 9)

    # Draw the golden spiral
    pos(250, 0)
    tina.pensize(15)
    tina.pencolor("gold")
    for i in range(40):
        tina.left(5)
        tina.forward(25)

    pos(-250, 0)
    tina.pensize(15)
    tina.pencolor("gold")
    for i in range(40):
        tina.left(5)
        tina.forward(25)

    # Writing text on the screen
    tina.penup()
    tina.goto(-480, 300)  # Position text in the upper left corner
    tina.color("Deeppink")
    tina.write("Happy Raksha Bandhan", align="left", font=("Arial", 35, "bold"))

    tina.penup()
    tina.goto(480, -300)  # Position text in the lower right corner
    tina.color("Blue")
    tina.write("You are being wished by ~ ", align="right", font=("Arial", 35, "bold"))

    tina.goto(500, -350)
    tina.color("Orange")
    tina.write("Brati", align="right", font=("Arial", 35, "bold"))
    tina.hideturtle()

    # Stop the music after the drawing is complete
    pygame.mixer.music.stop()

# Draw the Rakhi
draw_rakhi()

# End the Turtle graphics window
turtle.done()
