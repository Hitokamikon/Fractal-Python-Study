import numpy as np
import string
import sys
import os
from numbers import *

sys.path.append(os.path.join(os.getcwd(),'myproject/plot'))
sys.path.append(os.path.join(os.getcwd(),'myproject/l-system'))

import plot as plot
from l_system import *

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = [u'simHei']   # 显示中文
plt.rcParams['axes.unicode_minus'] = False      # 解决负号问题

def draw_l_system_fractal(fractal : L_SystemFractal , name : string , order : int, ratio : float):
  #创建3D绘图
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')
  current_order = 1
  result = fractal.axiom

  while current_order <= order:
    result = fractal.system.produce(result)
    # print(result)
    curves = fractal.turtle.run(result)

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


draw_l_system_fractal(create_koch_curve() , "科赫曲线" , 5 , 3)
draw_l_system_fractal(create_koch_snowflake() , "科赫雪花" , 5 , 3)
draw_l_system_fractal(create_sierpinski_triangle() , "谢尔宾斯基三角" ,5 , 3)
draw_l_system_fractal(create_sierpinski_carpet() , "谢尔宾斯基方毯" ,4 , 3)
draw_l_system_fractal(create_second_koch_island() , "二次科赫岛" ,5 , 4)
draw_l_system_fractal(create_pentigree() , "Pentigree分形" ,5 , 3)

draw_l_system_fractal(create_peano_curve_l() , "Peano L曲线" ,5 , 3)
draw_l_system_fractal(create_peano_curve_r() , "Peano R曲线" ,5 , 3)
draw_l_system_fractal(create_dragon_curve() , "龙曲线" ,15 , 1)

draw_l_system_fractal(create_hilbert_curve() , "希尔伯特曲线" , 5 , 2)

draw_l_system_fractal(L_SystemFractal( Turtle(1,np.pi / 6), L_System([Production("f" , "f[-f]f[+f]f")]) , "+++f") , "树" , 5 , 3)
draw_l_system_fractal(L_SystemFractal( Turtle(1,np.pi / 4 , s = 0.5), L_System([Production("f" , "g[+f]-f")]) , "++f") , "年龄树" , 5 , 1)
draw_l_system_fractal(L_SystemFractal( Turtle(1,np.pi / 9 , s = 1), L_System([Production("f" , "h+h+h+h+h+h+") , Production("h" , "[g+g+g+g[---h-x]+++++g]") , Production("x" , "[g+g+g+g[---x]+++++g++++++++g]")]) , "ffff") , "鹦鹉螺" , 5 , 1.5)

draw_l_system_fractal(L_SystemFractal( Turtle(1,np.pi / 8), L_System([Production("f" , "f[-f]f[+f]f" , p = 0.3333) , Production("f" , "f[-f]f[+f[-f]]" , p = 0.3333) , Production("f" , "ff+[+f-f-f]-[-f+f+f]" , p = 1)]) , "++++f") , "随机树" , 5 , 3)
