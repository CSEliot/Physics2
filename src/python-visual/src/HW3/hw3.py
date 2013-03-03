# coding: utf-8
'''
Created on Feb 8, 2013

@author: eliot2
'''

from __future__ import division
from visual import *
scene.background = color.white
scene.width = 800
scene.height = 800

def grid(max=10, rad=0.03):
    gray = (0.8, 0.8, 0.8)
    for x in range(-max, max + 1, 1):  # # parallel to z axis,  vary x
        cylinder(pos=(x, 0, -max), axis=(0, 0, 2 * max), radius=rad, color=gray, opacity=0.2)
    for z in range(-max, max + 1, 1):  # # parallel to x axis, vary z
        cylinder(pos=(-max, 0, z), axis=(2 * max, 0, 0), radius=rad, color=gray, opacity=0.2)
    for y in range(-max, max + 1, 1):  # # parallel to z axis, vary y
        cylinder(pos=(0, y, -max), axis=(0, 0, 2 * max), radius=rad, color=gray, opacity=0.2)
    for z in range(-max, max + 1, 1):  # # parallel to y axis, vary z
        cylinder(pos=(0, -max, z), axis=(0, 2 * max, 0), radius=rad, color=gray, opacity=0.2)

def axes(max=10, rad=0.1):
    xaxis = cylinder(color=(1, 0, 0), pos=(-max, 0, 0), axis=(2 * max, 0, 0), radius=rad)
    xlbl = label(pos=(11, 0, 0), text="X", color=color.red, opacity=0, height=30)
    yaxis = cylinder(color=color.green, pos=(0, -max, 0), axis=(0, 2 * max, 0), radius=rad)
    ylbl = label(pos=(0, 11, 0), text="Y", color=color.green, opacity=0, height=30)
    zaxis = cylinder(color=color.blue, pos=(0, 0, -max), axis=(0, 0, 2 * max), radius=rad)
    xlbl = label(pos=(0, 0, 11), text="Z", color=color.blue, opacity=0, height=30)



grid()  # # if you don't want a grid, comment out this line
axes()


basketball_pos = vector(-4, 2, 5)
volleyball_pos = vector(3, 1, -2)
origin = vector(0, 0, 0)
bball_vball_difference = volleyball_pos - basketball_pos
basketball = sphere(pos=(basketball_pos), radius=1, color=color.orange)
arrow_to_basketball = arrow(pos=(origin), axis=(basketball_pos), color=color.black)
volleyball = sphere(pos=(volleyball_pos), radius=1, color=color.white)
arrow_to_volleyball = arrow(pos=(origin), axis=(volleyball_pos) , color=color.black)
arrow_to_volleyball_from_basketball = arrow(pos=(basketball_pos), axis=(bball_vball_difference), color=color.black)
print "Position of the basketball: {0} ".format(basketball_pos)
print "Position of the volleyball: {0} ".format(volleyball_pos)
print "Arrow Stats:                  __TIP__    |   __TAIL__    "
print "arrow_to_basketball:        {0}   |   {1}".format(basketball_pos, origin)
print "arrow_to_volleyball:        {0}   |   {1}".format(volleyball_pos, origin)
print "arrow_to_bball_from_vball:  {0}   |   {1}".format(bball_vball_difference, basketball_pos)