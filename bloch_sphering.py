'''
Version 1.0
7.16.2019
Creates a front end animation of a bloch sphere with the following parameters:
animate(i): To animate or plot at each frame, 'i'.
(iterable): A post-processed list to iterate over which serve as the frame parameters to the animate function.
interval: The time (in ms) delay between each frame of the animation.
<step count>: The number of steps taken by the animate function, ie, the length of the iterable.
fps (frames per second): The "smoothness" of the animation. Is calculated by: <step count> * 1000/interval

@author: Amol Pant
'''
from qutip import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

class Animate:

    def flow(self):
        data = []
        fig = figure()
        ax = Axes3D(fig, azim=-40,elev=30)
        sphere = Bloch(axes=ax)
        print('x')

    '''Frame to be drawn at each step of the iterable.
    '''
    def animate(self, i):
        self.sphere.clear()
        self.sphere.add_states(i)
        # self.sphere.add_vectors([0,np.sin(i),np.sin(i) + np.cos(i)])
        # sphere.add_points([sx[:i+1],sy[:i+1],sz[:i+1]])
        self.sphere.make_sphere()
        return self.ax

    '''Initialization function.
    '''
    def init(self):
        self.sphere.vector_color = ['g']
        return self.ax

    '''Function that is called when the Animation object needs to be animated.
    '''
    def animation(self):
        # data = []
        self.fig = figure()
        self.ax = Axes3D(self.fig, azim=-40,elev=30)
        plt.subplots_adjust(left=0.1, bottom=0.01)
        self.sphere = Bloch(axes=self.ax)

        axSlider1 = plt.axes([0.1, 0.1, 0.8, 0.02])
        slder1 = Slider(axSlider1, 'slider 1', valmin=0, valmax=100)

        anim_running = True

        self.ani = animation.FuncAnimation(self.fig, self.animate, self.data,
        init_func=self.init,interval=1.0,
        repeat=False)

        def onClick(event):
            nonlocal anim_running
            if anim_running:
                self.ani.event_source.stop()
                anim_running = False
            else:
                self.ani.event_source.start()
                anim_running = True

        self.fig.canvas.mpl_connect('button_press_event', onClick)

        # ani.save('basic_animation.mp4', fps=25)
        self.sphere.show()

    '''Constructor. Called with the array of data that is inputted to create the animation object
    that uses the data over a constant time step.
    '''
    def __init__(self, data):
        self.data = data
