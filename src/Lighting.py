'''
Examples using Sense HAT animations: circle, triangle, line, and square functions.

By Ethan Tamasar, 5/15/2017
'''



from sense_hat import SenseHat
import time
import numpy as np
import time
import ect
from random import randint
import sys

sense = SenseHat()

w = [150, 150, 150]
b = [0, 0, 255]
e = [0, 0, 0]


# create empty screen
image = np.array([
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
])



'''
Demonstrate a bouncing ball
It will draw the ball, erase it, and then draw another ball in a different position
'''


for x in range(0,7):
    ect.cell(image,[0,x],[randint(0,255), randint(0,255), randint(0,255)],0.1)
    ect.cell(image,[0,x],e,0.1)
for x in range(7,0, -1):
    ect.cell(image,[0,x],[randint(0,255), randint(0,255), randint(0,255)],0.1)
    ect.cell(image,[0,x],e,0.1)


# triangles
ect.triangle(image,[0,0],[3,3],[0,6],[0,0,255], 1)
ect.triangle(image,[6,0],[3,3],[6,6],[0,0,255], 1)
image = ect.clear(image)


# moving circles
for y in range(5):
    ect.circle(image,(3,4), 2, w, .1)
    ect.circle(image,(3,4), 2, e, 0)
    ect.circle(image,(4,5), 3, w, .1)
    ect.circle(image,(4,5), 3, e, 0)
    ect.circle(image,(5,6), 3, w, .1)
    ect.circle(image,(5,6), 3, e, 0)
    ect.circle(image,(6,7), 3, w, .1)
    ect.circle(image,(6,7), 3, e, 0)
    ect.circle(image,(7,8), 3, w, .1)
    ect.circle(image,(7,8), 3, e, 0)
    ect.circle(image,(8,9), 3, w, .1)
    ect.circle(image,(8,9), 3, e, 0)
    ect.circle(image,(1,2), 2, w, .1)
    ect.circle(image,(1,2), 2, e, 0)


# colorful squares
for x in range(5):
    ect.square(image, [0,0], [7,0], [7,7],[0,7],[randint(0,255),randint(0,255),randint(0,255)],.01)
    ect.square(image, [1,1], [6,1], [6,6],[1,6],[randint(0,255),randint(0,255),randint(0,255)],.01)
    ect.square(image, [2,2], [5,2], [5,5],[2,5],[randint(0,255),randint(0,255),randint(0,255)],.01)


# clear screen with squares
ect.square(image, [0,0], [7,0], [7,7],[0,7],e,.01)
ect.square(image, [1,1], [6,1], [6,6],[1,6],e,.01)
ect.square(image, [2,2], [5,2], [5,5],[2,5],e,.01)

# more moving circles
ect.circle(image,(3,4), 3, w, 1)
ect.circle(image,(3,4), 3, e, 0)
ect.circle(image,(4,4), 3, w, 1)
ect.circle(image,(4,4), 3, e, 0)
ect.circle(image,(3,4), 3, w, 1)
ect.circle(image,(3,4), 3, e, 0)


'''
This subroutine first draw a circle with an epicenter of (4,4). It then has a radius of 3 followed by
random colors done with [randint(0,255), randint(0,255), randint(0,255)] this can generate a random number
from 0 to 255. For instance, it might generate [10,233,100]. The last value of 0.1 is the number of second
it will keep the image displayed. 
'''

for x in range(0, 10):
    ect.circle(image,(4,4), 3, [randint(0,255), randint(0,255), randint(0,255)], 0.1) 
    ect.circle(image,(4,4), 2, [randint(0,255), randint(0,255), randint(0,255)], 0.1)
    ect.circle(image,(4,4), 1, [randint(0,255), randint(0,255), randint(0,255)], 0.1)    



ect.circle(image,(4,4), 3, w, 1)
ect.circle(image,(4,4), 3, b, 1)
ect.circle(image,(4,4), 3, w, 1)
ect.circle(image,(4,4), 3, b, 1)
ect.circle(image,(4,4), 2, b, 1)
ect.circle(image,(4,4), 1, b, 1)
ect.circle(image,(4,4), 1, e, 1)
ect.circle(image,(4,4), 2, e, 1)
ect.circle(image,(4,4), 3, e, 1)



# stack images ontop of each other

for x in range(0, 10):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    image1 = ect.circle(image,(4,4), 3, [r, g, b], 0.1) 
    image2 = ect.circle(image1,(4,4), 2, [r, g, b], 0.1)
    image3 = ect.circle(image2,(4,4), 1, [r, g, b], 0.1)    

image3 = ect.clear(image3)
