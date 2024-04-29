import numpy as np
import string
import sys
import os

sys.path.append(os.path.join(os.getcwd(),'myproject/plot'))
sys.path.append(os.path.join(os.getcwd(),'myproject/l-system'))

import plot as plot
from parameter_l_system import *

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = [u'simHei']   # 显示中文
plt.rcParams['axes.unicode_minus'] = False      # 解决负号问题

def draw_parameter_l_system_fractal(system : Parameter_L_System , axiom : list[Parameter] , name : string , order , ratio):
    
    #创建3D绘图
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    turtle = ParameterTurtle(1 , np.pi / 2.1)
    current_order = 1
    result = axiom
    while current_order <= order:
        result = system.produce(result)
        curves = turtle.run(result)

        curves2 = []
        o = ratio ** current_order
        for curve in curves:
            curve2 = []
            curves2.append(curve2)
            for p in curve: 
                curve2.append((current_order , p[0] / o , p[1] / o))
        plot.draw_3d_curves(ax , name + str(current_order) , curves2)
        current_order = current_order + 1
    plt.show()

# f(x) → f(x)+f(2x)--f(2x)+f(4x)
system = Parameter_L_System([ParameterProduction(Parameter("f" , [1]) , lambda parameter : True , [
    lambda p : Parameter("f" , [p.paras[0]]) , 
    lambda p : Parameter("+" , []) , 
    lambda p : Parameter("f" , [p.paras[0] * 2]) , 
    lambda p : Parameter("-" , []) , 
    lambda p : Parameter("-" , []) , 
    lambda p : Parameter("f" , [p.paras[0] * 2]) , 
    lambda p : Parameter("+" , []) , 
    lambda p : Parameter("f" , [p.paras[0] * 4]) , 
    ])])

result = [Parameter("f" , [1])]

draw_parameter_l_system_fractal(system , result , "a" , 5 , 1)