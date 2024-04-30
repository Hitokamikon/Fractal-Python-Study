import numpy as np
import string
import sys
import os
from numbers import *

sys.path.append(os.path.join(os.getcwd(),'myproject/plot'))
sys.path.append(os.path.join(os.getcwd(),'myproject/Mandelbort'))

import plot as plot
from mandelbrot import *

import matplotlib.pyplot as plt

def draw_mandelbrot(xMin : float , xMax : float , yMin : float , yMax : float , interval : float , N : int):
    fig=plt.figure() #创建画布
    x = xMin
    xs = []
    ys = []
    while x <= xMax:
        y = yMin
        while y <= yMax:
            julia = mandelbrot_set_judge(N , complex(x,y))
            if julia == N:
                xs.append(x)
                ys.append(y)
            y+=interval
        x+=interval

    plt.scatter(xs,ys , s=0.1)
    plt.show()


draw_mandelbrot(-10,10 , -10 , 10 , 0.01 , 25)

