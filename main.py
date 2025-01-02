import turtle
import random

#set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

#create a turtle object
pen = turtle.Turtle()
pen.speed(0)

#function to draw a star
def draw_star(size, color):
    pen.color(color)
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
        pen.forward(size)
        pen.right(72 - 144)
    pen.end_fill()

#function to draw a pattern
def draw_pattern(repetitions, size_variation, colors):
    for _ in range(repetitions):
#setting random sizes of each star
        size = random.uniform(50, size_variation)
        color = random.choice(colors)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
#draw the star by random parameters
        draw_star(size, color)

#get user input
repetitions = int(input("Enter the number of repetitions: "))
size_variation = int(input("Enter the maximum size: "))
colors = input("Enter the colors: ").split(',')

#draw the pattern by user input
draw_pattern(repetitions, size_variation, colors)

pen.hideturtle()
turtle.done()