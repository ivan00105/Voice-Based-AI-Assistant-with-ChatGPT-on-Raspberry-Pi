'''
Sense HAT graphic animations: circle, triangle, line, and square functions.

By Ethan Tamasar, 5/15/2017
'''

from sense_hat import SenseHat
import time
import numpy as np
import time
from random import randint

def circle(image, position, radius, color, timer):

    sense = SenseHat()
    
    width, height = 8, 8
    a, b = position[0], position[1]
    r = radius
    EPSILON = 1.2

    image2 = image.reshape(8,8,3)

    # draw the circle
    for y in range(height):
        for x in range(width):
            if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:
                image2[y][x] = color

    image3 = image2.reshape(64,3)
    sense.set_pixels(image3)
    time.sleep(timer)
    
    return image3


def cell(image, position, color, timer):

    sense = SenseHat()

    image2 = image.reshape(8,8,3)
    image2[position[0],position[1]] = color
    image3 = image2.reshape(64,3)

    sense.set_pixels(image3)

    time.sleep(timer)


def line(image, point1, point2, color, timer):

    sense = SenseHat()
    image2 = image.reshape(8,8,3)

    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    dx = (x2 - x1) 
    dy = (y2 - y1) 

    if abs(dx) > abs(dy) :
        steps = abs(dx) 
    else :
        steps = abs(dy) 

    Xincrement = dx / steps
    Yincrement = dy / steps
    x = x1
    y = y1
    
    for v in range(steps + 1):
        image2[y,x] = color 
        x = x + Xincrement;
        y = y + Yincrement;
    
    image3 = image2.reshape(64,3)
    sense.set_pixels(image3)
    time.sleep(timer)
    return image3



def triangle(image, point1, point2, point3, color, timer):

    sense = SenseHat()
    image2 = image.reshape(8,8,3)

    line(image2, point2, point1, color, timer)
    line(image2, point3, point2, color, timer)
    line(image2, point1, point3, color, timer)

    image3 = image2.reshape(64,3)
    sense.set_pixels(image3)
    time.sleep(timer)

    return image3



def square(image, point1, point2, point3, point4, color, timer):

    sense = SenseHat()
    image2 = image.reshape(8,8,3)

    line(image2, point1, point2, color, 0)
    line(image2, point2, point3, color, 0)
    line(image2, point3, point4, color, 0)
    line(image2, point4, point1, color, 0)

    image3 = image2.reshape(64,3)
    sense.set_pixels(image3)
    time.sleep(timer)

    return image3



def clear(image):

    sense = SenseHat()

    e = [0, 0, 0]
    
    image2 = np.array([
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ])

    image = image2

    sense.set_pixels(image)

    return image



def blinking_circle(image,position):

    sense = SenseHat()

    for x in range(0, 10):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        image1 = circle(image,(position[0],position[1]), 3, [r, g, b], 0.1) 
        image2 = circle(image1,(position[0],position[1]), 2, [r, g, b], 0.1)
        image3 = circle(image2,(position[0],position[1]), 1, [r, g, b], 0.1)  
