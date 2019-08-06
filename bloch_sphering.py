'''
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
# import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from player import Player

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)

        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

class Animate:

    '''Constructor. Called with the array of data that is inputted to create the animation object
    that uses the data over a constant time step.
    '''
    def __init__(self, data):
        self.data = data
        self.counter = 0

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
        self.counter = 0
        self.fig = figure(figsize=(5,5))
        self.ax = Axes3D(self.fig, rect=(0.4, 0.4, 0.5, 0.5), azim=-40,elev=30)
        self.sphere = Bloch(axes=self.ax)

        if self.sphere._rendered:
            self.sphere.axes.clear()

        self.sphere._rendered = True

        if self.sphere.background:
            self.sphere.axes.clear()
            self.sphere.axes.set_xlim3d(-1.3, 1.3)
            self.sphere.axes.set_ylim3d(-1.3, 1.3)
            self.sphere.axes.set_zlim3d(-1.3, 1.3)
        else:
            self.sphere.plot_axes()
            self.sphere.axes.set_axis_off()
            self.sphere.axes.set_xlim3d(-0.7, 0.7)
            self.sphere.axes.set_ylim3d(-0.7, 0.7)
            self.sphere.axes.set_zlim3d(-0.7, 0.7)

        self.sphere.plot_back()
        self.sphere.plot_front()

        self.ani = Player(self.fig, self.test, init_func=self.init, mini=0, maxi=len(self.data)-1)

        plt.close(fig=0)
        self.sphere.show()
        # plt.close()

    def test(self, i):
        self.sphere.clear()
        self.sphere.add_states(self.data[i])
        self.plot_vecs()
        self.sphere.clear()
        return self.ax

    def plot_vecs(self):
        for k in range(len(self.sphere.vectors)):
            xs3d = self.sphere.vectors[k][1] * array([0, 1])
            ys3d = -self.sphere.vectors[k][0] * array([0, 1])
            zs3d = self.sphere.vectors[k][2] * array([0, 1])

            color = self.sphere.vector_color[mod(k, len(self.sphere.vector_color))]

            if self.sphere.vector_style == '':
                self.sphere.axes.plot(xs3d, ys3d, zs3d,
                               zs=0, zdir='z', label='Z',
                               lw=self.sphere.vector_width, color=color)
            else:
                a = Arrow3D(xs3d, ys3d, zs3d,
                            mutation_scale=self.sphere.vector_mutation,
                            lw=self.sphere.vector_width,
                            arrowstyle=self.sphere.vector_style,
                            color=color)

                if (self.counter != 0):
                    self.curr_state.remove()
                self.curr_state = a
                self.sphere.axes.add_artist(a)
                self.counter += 1
