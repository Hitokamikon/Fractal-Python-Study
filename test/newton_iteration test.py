import numpy as np
import string
import sys
import os
from numbers import *

sys.path.append(os.path.join(os.getcwd(),'myproject/plot'))
sys.path.append(os.path.join(os.getcwd(),'myproject/Newton Iteration'))

import plot as plot
from newton_iteration import *

import matplotlib.pyplot as plt

def draw_newton_iteration(xMin : float , xMax : float , yMin : float , yMax : float , interval : float , a : list[complex] , N : int , epsilon : float):
    fig=plt.figure() #创建画布
    x = xMin
    xs = []
    ys = []
    while x <= xMax:
        y = yMin
        while y <= yMax:
            value = newton_iteration_judge(a , complex(x,y) , N , epsilon)
            if value == N:
                xs.append(x)
                ys.append(y)
            y+=interval
        x+=interval

    plt.scatter(xs,ys , s=0.1)
    plt.show()


draw_newton_iteration(-2,2 , -1.5 , 1.5 , 0.01 , [complex(-1,0) , complex(0,0) , complex(0,0) , complex(1,0)] , 9 , 0.00001)

