import sys
import os
import numpy as np

import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.getcwd(),'myproject/IFS'))

from ifs2d import *

ifs = IFS2d([AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0 , 0) , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0) , AffineTransform2d(0.5 , 0 , 0 , 0.5 , 0.5 , 0.5)])

i = 0
result = [Point2D(0.75 , 0.25)]
#创建3D绘图
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

while i < 7:
  i += 1
  result = ifs.process_point(result)
  x_values = np.full(len(result) , i)
  y_values = [point.x for point in result]
  z_values = [point.y for point in result]
  ax.scatter(x_values , y_values , z_values)
plt.show()




