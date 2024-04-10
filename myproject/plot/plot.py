# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
import string
from array import array
import numpy as np
import matplotlib.pyplot as plt
# mpl.rcParams['legend.fontsize'] = 10

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 200)
z = np.linspace(-2, 2, 200)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()

def draw_plot(label :string, x:array , y:array , z:array):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(x, y, z, label=label)
    ax.legend()
    plt.show()

draw_plot('parametric curve' , x , y , z)