from turtle import *
setup(width=2000, height=1800, startx=1000, starty=150)
pensize(2)

speed(10)
penup()
back(750)
pendown()
color('blue', 'green')

begin_fill()
for i in range(19):
    forward(1500)
    left(180 - 180/19)
end_fill()
hideturtle()
done()
