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


fig=plt.figure() #创建画布
x = -10
xs = []
ys = []
while x < 10:
    y = -10
    while y < 10:
        julia = fill_julia_set_judge(10 , complex(-0.95,0.1) , complex(x,y))
        if julia == 10:
            xs.append(x)
            ys.append(y)
        y+=0.005
    x+=0.005

plt.scatter(xs,ys , s=0.1)
plt.show()
