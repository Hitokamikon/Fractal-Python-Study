import sys
import os
import numpy as np
import string

import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.getcwd(),'myproject/IFS'))
sys.path.append(os.path.join(os.getcwd(),'myproject/plot'))

from ifsp2d import *
import plot as plot


plt.rcParams['font.sans-serif'] = [u'simHei']   # 显示中文
plt.rcParams['axes.unicode_minus'] = False      # 解决负号问题

def draw_ifsp2d(ifsp2d : IFSP2d , name : string , order : int):
  i = 0
  result = Point2D(0.75 , 0.25)
  #创建3D绘图
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')

  x_values = []
  y_values = []
  z_values = []
  while i < order:
    i += 1
    result = ifsp2d.process_point(result)
    x_values.append(0)
    y_values.append(result.x)
    z_values.append(result.y)
  ax.scatter(x_values , y_values , z_values , s = 0.3)
  plt.title(name)
  plt.show()

draw_ifsp2d(IFSP2d([(0.3333 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0 , 0)) , 
             (0.3333 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0)) , 
             (0.3335 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0.5))
             ]) , "谢尔宾斯基三角" , 10000)

draw_ifsp2d(IFSP2d([(0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0 , 0)) , 
             (0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0.666 , 0)) , 
             (0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0.333 , 0.333)),
             (0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0 , 0.666)),
             (0.2 , AffineTransform2d(0.333 , 0 , 0 , 0.333 , 0.666 , 0.666)),
             ]) , "Box分形" , 10000)

draw_ifsp2d(IFSP2d([(0.01 , AffineTransform2d(0 , 0 , 0 , 0.16 , 0 , 0)) , 
             (0.85 , AffineTransform2d(0.85 , 0.1 , -0.05 , 0.85 , 0 , 0.6)) , 
             (0.07 , AffineTransform2d(-0.2 , 0.26 , 0.23 , 0.22 , 0 , 0.6)),
             (0.07 , AffineTransform2d(0.21 , -0.25 , 0.25 , 0.21 , 0 , 0.44)),
             ]) , "分形蕨" , 10000)

draw_ifsp2d(IFSP2d([(0.1 , AffineTransform2d(0.14 , 0.01 , 0 , 0.51 , -0.08 , -1.31)) , 
             (0.35 , AffineTransform2d(0.43 , 0.52 , -0.45 , 0.5 , 1.49 , -0.75)) , 
             (0.35 , AffineTransform2d(0.45 , -0.49 , 0.47 , 0.47 , -1.62 , -0.74)),
             (1 , AffineTransform2d(0.49 , 0 , 0 , 0.51 , 0.02 , 1.62)),
             ]) , "枫叶" , 50000)


