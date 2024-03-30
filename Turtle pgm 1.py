import turtle
import random

t = turtle.Turtle()

colors=['violet','blue','green','yellow','orange','red']

def draw_star(size):
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

x = -200
y = 0
n=int(input("Enter limit: "))
for i in range(n):
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_star(50)  
    x += 100
    
turtle.done()

