from turtle import *

Color = {"blue":[1,0,0],"red":[0,1,0],"green":[0,0,1],"yellow":[1,1,0],"cyan":[0,1,1],"light_purple":[1,0,1],"white":[1,1,1],"black":[0,0,0]}

def rectangle(l,L,color):
    fillcolor(Color[color])
    begin_fill()
    for i in range(2):
        forward(l)
        right(90)
        forward(L)
        right(90)
    end_fill()

def triangle(l,color):
    fillcolor(Color[color])
    begin_fill()
    for i in range(3):
        forward(l)
        right(120)
    end_fill()

def cercle(r,color):
    fillcolor(Color[color])
    begin_fill()
    circle(r)
    end_fill()