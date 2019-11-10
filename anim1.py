#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:05:38 2019

@author: sapronov
"""

import math
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(-50, 150), ylim=(-50, 150))
ax.set_title('Drawing arm')
ax.set_aspect('equal', 'box')
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

def animate2(i):
    x = i
    y = 100
    [th1, th2, x_j, y_j] = invkin2(x, y, DEGREES)

    xd = [0, x_j, x]
    yd = [0, y_j, y]

    line.set_data(xd, yd)

    print(i)
    return line,

RADIANS = 0
DEGREES = 1

l1 = 10 #Length of link 1
l2 = 10 #length of link 2

#IK for just the 2 links
def invkin2(x, y, angleMode=DEGREES):
    """Returns the angles of the first two links
    in the robotic arm as a list.
    returns -> (th1, th2)
    input:
    x - The x coordinate of the effector
    y - The y coordinate of the effector
    angleMode - tells the function to give the angle in
                degrees/radians. Default is degrees
    output:
    th1 - angle of the first link w.r.t ground
    th2 - angle of the second link w.r.t the first"""

    #stuff for calculating th2
    r_2 = x**2 + y**2
    l_sq = l1**2 + l2**2
    term2 = (r_2 - l_sq)/(2*l1*l2)
    term1 = ((1 - term2**2)**0.5)*-1
    #calculate th2
    th2 = math.atan2(term1, term2)
    #optional line. Comment this one out if you
    #notice any problems
    th2 = -1*th2

    #Stuff for calculating th2
    k1 = l1 + l2*math.cos(th2)
    k2 = l2*math.sin(th2)
    r  = (k1**2 + k2**2)**0.5
    gamma = math.atan2(k2,k1)
    #calculate th1
    th1 = math.atan2(y,x) - gamma

    x_j = l1 * math.cos(th1)
    y_j = l1 * math.sin(th1)

    drawPlot = False
    if (drawPlot):
        plt.show()
        plt.plot([0, x_j, x], [0, y_j, y])

    if(angleMode == RADIANS):
        return th1, th2, x_j, y_j
    else:
        return math.degrees(th1), math.degrees(th2), x_j, y_j

def plot_arm(th1, th2, x, y):
    x_j = l1 * math.cos(th1)
    y_j = l1 * math.sin(th1)

    #fig2 = plt.figure()
    #print([0, x_j, x], [0, y_j, y])
    #plt.plot([0, x_j, x], [0, y_j, y])
    #plt.show()
    plt.plot([0, x_j, x], [0, y_j, y])
    #plt.plot([0, 100, 100], [0, 0, 100])
    #plt.show()

if __name__ == "__main__":
    print(invkin2(0, 0, DEGREES))

    numFrames = 100

    for i in np.linspace(0, numFrames, numFrames+1):
        [th1, th2, xj, yj] = invkin2(0, 0, DEGREES)
        plot_arm(th1, th2, i, 100)

        #anim = FuncAnimation(fig, animate, init_func=init,
        #                       frames=200, interval=20, blit=True)
        #anim.save('sine_wave.gif', writer='imagemagick')
        anim = FuncAnimation(fig, animate2, init_func=init,
                             frames=50, interval=100, blit=True)
        # anim.save('arm.gif', writer='imagemagick')
    plt.show()
