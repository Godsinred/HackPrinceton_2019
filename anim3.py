#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:05:38 2019


https://ashwinnarayan.blogspot.com/2014/07/inverse-kinematics-for-2dof-arm.html
https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
@author: Leonid Sapronov
Kasia Krzyzanska
Dominic Curcio

"""

import math
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


angleList = []
letters = [(0,0),(0,20),(10,20),(10,10),(0,10),(10,10),(10,0),(15,0),(15,20),(25,20),(25,10),(15,10),(25,10),(25,0)]
numFrames = len(letters)

fig = plt.figure()
ax = plt.axes(xlim=(-10, 100), ylim=(-100, 50))
ax.set_title('Drawing arm')
ax.set_aspect('equal', 'box')
line, = ax.plot([], [], lw=3)

RADIANS = 0
DEGREES = 1

l1 = 100 #Length of link 1
l2 = 100 #length of link 2


def init():
    line.set_data([], [])
    return line,

def animate2(i):
    #x = endpointList[i][0]
    #y = endpointList[i][1]

    endpointList = letters

    x = endpointList[i][0]
    y = endpointList[i][1]
     
    [th1, th2, x_j, y_j] = invkin2(x, y, DEGREES)

    angleList.append((th1, th2))
     
    x_val = [n[0] for n in endpointList[:i+1]]
    y_val = [n[1] for n in endpointList[:i+1]]

    plt.plot(x_val, y_val,'m', zorder = 1)

    plotDot()
    
    xd = [0, x_j,x ]
    yd = [0, y_j,y ]
    
    line.set_data(xd, yd)
    return line,



#IK for just the 2 links
def invkin2(x, y, angleMode=DEGREES):
    """"
    Returns the angles of the first two links
    in the robotic arm as a list.
    returns -> (th1, th2)
    input:
    x - The x coordinate of the effector
    y - The y coordinate of the effector
    angleMode - tells the function to give the angle in
                degrees/radians. Default is degrees
    output:
    th1 - angle of the first link w.r.t ground
    th2 - angle of the second link w.r.t the first 
    """

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

    if(angleMode == RADIANS):
        return th1, th2, x_j, y_j
    else:
        return math.degrees(th1), math.degrees(th2), x_j, y_j
    
         
def plotDot():
    xdot = []
    ydot = []

   # rangeVal = int(numFrames/7)*75
    
    for n in range (10):
        xdot.append(n*15 -2.5)
        ydot.append(0)

    plt.scatter(xdot, ydot, c='w', s=45, zorder = 2)

if __name__ == "__main__":
   
    
    anim = FuncAnimation(fig, animate2, init_func=init,
                         frames =numFrames, interval=100, blit=True)
    anim.save('arm.gif', writer='imagemagick')
    print(angleList)
