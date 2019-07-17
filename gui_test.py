import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import animatplot as amp
from qutip import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

x = np.linspace(0, 1, 50)
t = np.linspace(0, 1, 20)

X, T = np.meshgrid(x, t)
Y = np.sin(2*np.pi*(X+T))

data = []
fig = figure()
ax = Axes3D(fig, azim=-40,elev=30)
sphere = Bloch(axes=ax)

def animate(i):
    sphere.clear()
    # sphere.add_states(i)
    sphere.add_vectors([0,np.sin(i),np.sin(i) + np.cos(i)])
    # sphere.add_points([sx[:i+1],sy[:i+1],sz[:i+1]])
    sphere.make_sphere()
    return ax

def init():
    sphere.vector_color = ['r']
    return ax

ani = animation.FuncAnimation(fig, animate, np.linspace(1,pi,100),
                                    init_func=init,interval=1.0,
                                    repeat=False)
anim = amp.Animation(ani)

anim.controls()

sphere.show()
