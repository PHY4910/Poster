from nbody import *
from random import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from sys import argv
from time import sleep

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
#ax.set_xlim(0, 50)
#ax.set_ylim(0, 50)

s = System.read_binary(argv[1])

x = s.all_x()
y = s.all_y()

line, = ax.plot(x, y, ',')#, markersize=5, linestyle='none', mfc="grey", mec="black", mew=0.5)
#line2, = ax.plot(x[0], y[0], color="red", marker="o", markersize=5, linestyle='none', mfc="red", mec="red", mew=0.5)

def update(fname):
    #sleep(0.1)
    s = System.read_binary(fname)
    x = s.all_x()
    y = s.all_y()
    
    line.set_data(x, y)
    #line2.set_data(x[0], y[0])      

if len(argv) > 2:
    ani = animation.FuncAnimation(fig, update, frames=argv[2:], interval=20)

plt.show()

