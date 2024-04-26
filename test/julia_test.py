import numpy as np
import string
import sys
import os
from numbers import *

sys.path.append(os.path.join(os.getcwd(),'myproject/plot'))
sys.path.append(os.path.join(os.getcwd(),'myproject/Julia'))

import plot as plot
from julia import *

import matplotlib.pyplot as plt

def draw_fill_julia(xMin : float , xMax : float , yMin : float , yMax : float , interval : float , c : complex , N : int):
    fig=plt.figure() #创建画布
    x = xMin
    xs = []
    ys = []
    while x <= xMax:
        y = yMin
        while y <= yMax:
            julia = fill_julia_set_judge(N , c , complex(x,y))
            if julia == N:
                xs.append(x)
                ys.append(y)
            y+=interval
        x+=interval

    plt.scatter(xs,ys , s=0.1)
    plt.show()


draw_fill_julia(-10,10 , -10 , 10 , 0.01 , complex(-0.95 , 0.1) , 25)
draw_fill_julia(-10,10 , -10 , 10 , 0.01 , complex(-0.14 , 0.72) , 25)

