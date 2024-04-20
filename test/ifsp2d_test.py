import sys
import os
import numpy as np

import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.getcwd(),'myproject/IFS'))

from ifsp2d import *

ifs = IFSP2d([(0.3333 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0 , 0)) , 
             (0.3333 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0)) , 
             (0.3335 , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0.5))])

i = 0
result = Point2D(0.75 , 0.25)
#创建3D绘图
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x_values = []
y_values = []
z_values = []
while i < 10000:
  i += 1
  result = ifs.process_point(result)
  x_values.append(0)
  y_values.append(result.x)
  z_values.append(result.y)
ax.scatter(x_values , y_values , z_values)
plt.show()




