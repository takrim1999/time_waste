#!/usr/bin/python3
from turtle import *
# This is the decimal value of FFFFFF, white. 16777216

# Most important thing here is color,
# Thats why I'm writing it.
# I need to make a function with instruction that will show how to brute force colorcodes colorfully.

def init():
    shape("arrow")
    pensize(50)
    shapesize(15)
    setpos(0,-200)
    speed(10)

def draw(col):
    begin_fill()
    color(col)
    circle(200)
    end_fill()

def good_color(time):
    ## First we can brute force RGB indiividually.
    unit_time = 4
    desired_colors = int(int(time)/unit_time)
    highest_color = 2**8
    variations = 9
    if desired_colors < variations:
        variations = desired_colors

    interval = int(highest_color/desired_colors)
    for j in range(variations):
        if j==0:
            for i in range(0,highest_color,interval):
                draw("#0000"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:])
        elif j==1:
            for i in range(0,highest_color,interval):
                draw("#00"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:]+"00")
        elif j==2:
            for i in range(0,highest_color,interval):
                draw("#"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:]+"0000")
        elif j==3:
            for i in range(0,highest_color,interval):
                draw("#00FF"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:])
        elif j==4:
            for i in range(0,highest_color,interval):
                draw("#FF00"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:])
        elif j==5:
            for i in range(0,highest_color,interval):
                draw("#FF"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:]+"00")
        elif j==6:
            for i in range(0,highest_color,interval):
                draw("#00"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:]+"FF")
        elif j==7:
            for i in range(0,highest_color,interval):
                draw("#"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:]+"FF00")
        elif j==8:
            for i in range(0,highest_color,interval):
                draw("#"+"0"*(2-len(hex(i)[2:]))+hex(i)[2:]+"00FF")
init()
good_color(input("how many seconds you want to waste?\n>"))
done()
