#!/usr/bin/python3
from os import lstat
import random
from turtle import *
from unicodedata import name
speed(0)
colormode(255)
pensize(20)
color("white")
setpos(0,-200)
# shape("arrow")
# shapesize(5)
global lst
lst = [(255,255,255)]
def write_name(col):
    speed(0)
    color(lst[0])
    setpos(0,-30)
    color(col)
    write("BIG COLOR",align='center',font=('Arial',26,'normal'))
    color(lst[0])
    setpos(0,-200)
    lst.pop(0)

# textinput("NIM","NAME OF FIRST PLAYER")
for i in range(100):
    
    col = tuple([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    lst.append(col)
    write_name(col)
    speed(10)
    begin_fill()
    color(col) 
    circle(200)
    end_fill()

done()