# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
import string
from array import array
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import random
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

# draw_plot('parametric curve' , x , y , z)

def draw_2d_points(label: string , points : array):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # fig = plt.figure()
    x_values = [item[0] for item in points]
    y_values = [item[1] for item in points]
    # ax = fig.add_subfigure(projection = '2d')
    plt.plot(x_values , y_values , label=label)
    plt.legend()

def draw_3d_points(ax , label: string , points : array):
    x_values = [item[0] for item in points]
    y_values = [item[1] for item in points]
    z_values = [item[2] for item in points]
    
    ax.plot(x_values , y_values , z_values , label=label)
    ax.legend()

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#{:02x}{:02x}{:02x}'.format(r , g , b)

def draw_3d_curves(ax : axes , label: string , curves : array):
    i = 0
    color = generate_random_color()
    for curve in curves:
        x_values = [item[0] for item in curve]
        y_values = [item[1] for item in curve]
        z_values = [item[2] for item in curve]
        if i == 0:
          ax.plot(x_values , y_values , z_values , label=label , color = color)
        else:
          ax.plot(x_values , y_values , z_values , label="_nolegend_" , color = color)
            
        i = i + 1
    ax.legend()