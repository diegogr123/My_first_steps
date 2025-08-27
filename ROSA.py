from turtle import *
import colorsys as cs 

title ("para ti")
setup (900,800, 200,40)
speed(0)
tracer (10)
width(2)
bgcolor("black")


for j in range(25):
    for i in range (15):
        color (cs.hsv_to_rgb(i/15,j/25,1))
        right (90)
        circle(200-j*4,90)
        left(90)
        circle(200-j*4,90)
        right(180)
        circle(50,24)

hideturtle()
done()