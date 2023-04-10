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

while True:
    for x in range(5):
        ect.square(image, [0,0], [7,0], [7,7],[0,7],[randint(0,255),randint(0,255),randint(0,255)],.01)
        ect.square(image, [1,1], [6,1], [6,6],[1,6],[randint(0,255),randint(0,255),randint(0,255)],.01)
        ect.square(image, [2,2], [5,2], [5,5],[2,5],[randint(0,255),randint(0,255),randint(0,255)],.01)