from qutip import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from player import Player

class BlochModtesting:

    '''Constructor. Called with the array of data that is inputted to create the animation object
    that uses the data over a constant time step.
    '''
    def __init__(self, data):
        self.data = data

    '''Frame to be drawn at each step of the iterable.
    '''
    def animate(self, i):
        start = time.time()
        self.sphere.clear()
        cleared = time.time() - start
        self.sphere.add_states(self.data[i])
        added = time.time() - cleared - start
        self.sphere.make_sphere()
        print("Final: " + str(time.time() - start))
        print(" Clear " + str(cleared) + " Added " + str(added))
        return self.ax

    '''Initialization function.
    '''
    def init(self):
        self.sphere.vector_color = ['g']
        return self.ax


    '''Function that is called when the Animation object needs to be animated.
    '''
    def animation(self):
        self.fig = figure(figsize=(5,5))
        self.ax = Axes3D(self.fig, rect=(0.4, 0.4, 0.5, 0.5), azim=-40,elev=30)
        self.sphere = Bloch(axes=self.ax)

        # axSlider1 = plt.axes([0.5, 0.1, 0.3, 0.02])
        # slder1 = matplotlib.widgets.Slider(axSlider1, 'slider 1', valmin=0, valmax=100)

        self.ani = Player(self.fig, self.animate, init_func=self.init, mini=0, maxi=len(self.data)-1)

        # def update_slider(val):
        #     val_int = int(val)
        #     self.animate(val_int)
        #     self.fig.canvas.draw_idle()
        #
        # axSlider1 = self.fig.add_axes([0.5, 0.1, 0.3, 0.02])
        # slder1 = Slider(axSlider1, 'slider 1', valmin=0, valmax=len(self.data), valfmt="%0.0f")
        # val = int(slder1.val)
        # print("AASLDOFIUASDIOUFHASIJLDFH " + str(type(val)))
        # slder1.set_val(int(val))
        #
        # print("AASLDOFIUASDIOUFHASIJLDFH " + str(type(val)))
        # slder1.on_changed(update_slider)

        self.sphere.show()
