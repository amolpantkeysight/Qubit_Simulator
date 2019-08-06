'''
Is an Object which while create play and provde controls to some animation data that is fed. Uses matplotlib's FuncAnimation class
and creates the animation based on some function applied over some frames.
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.axes_grid1
import matplotlib.widgets
import time

class Player(FuncAnimation):
    def __init__(self, fig, func, frames=None, init_func=None, fargs=None,
                 save_count=None, mini=0, maxi=100, pos=(0.125, 0.92),**kwargs):
        self.i = 0
        self.min=mini
        self.max=maxi
        self.runs = True
        self.forwards = True
        self.fig = fig
        self.func = func
        self.buffer_interval = 0
        self.skipper = 1
        self.setup(pos)
        FuncAnimation.__init__(self,self.fig, self.func, frames=self.play(),
                                           init_func=init_func, fargs=fargs,
                                           save_count=save_count,interval=20, **kwargs )

    def play(self):
        while self.runs:
            # time.sleep(0)
            self.i = self.i+(self.forwards*self.skipper)-((not self.forwards)*self.skipper)

            if self.i < self.min:
                self.i = self.min
            if self.i > self.max:
                self.i = self.max
            self.slder1.set_val(self.i)
            if self.i > self.min and self.i < self.max:
                yield self.i
            else:
                self.stop()
                yield self.i

    def start(self):
        self.runs=True
        self.event_source.start()

    def stop(self, event=None):
        self.runs = False
        self.event_source.stop()

    def forward(self, event=None):
        if self.i >= self.min and self.i < self.max:
            self.forwards = True
            self.start()
    def backward(self, event=None):
        if self.i > self.min and self.i <= self.max:
            self.forwards = False
            self.start()
    def oneforward(self, event=None):
        self.forwards = True
        self.onestep()
    def onebackward(self, event=None):
        self.forwards = False
        self.onestep()

    def onestep(self):
        if self.i > self.min and self.i < self.max:
            self.i = self.i+self.forwards-(not self.forwards)
            self.slder1.set_val(self.i)
        elif self.i == self.min and self.forwards:
            self.i+=1
            self.slder1.set_val(self.i)
        elif self.i == self.max and not self.forwards:
            self.i-=1
            self.slder1.set_val(self.i)
        self.func(self.i)
        self.fig.canvas.draw_idle()

    def setup(self, pos):
        def update_slider(val):
            val_int = int(val)
            self.i = val_int
            self.func(val_int)
            self.fig.canvas.draw_idle()

        axSlider1 = self.fig.add_axes([0.5, 0.1, 0.3, 0.02])
        self.slder1 = matplotlib.widgets.Slider(axSlider1, 'slider 1', valmin=0, valmax=self.max-1, valfmt="%0.0f")
        val = int(self.slder1.val)
        self.slder1.set_val(int(val))
        self.slder1.on_changed(update_slider)

        axbox1 = self.fig.add_axes([0.3, 0.8, 0.05, 0.05])
        self.box1 = matplotlib.widgets.TextBox(axbox1, 'Speed: ', initial='1')

        def submit(t_value):
            t_val = int(eval(t_value))
            self.skipper = t_val

        self.box1.on_submit(submit)

        playerax = self.fig.add_axes([pos[0],pos[1], 0.22, 0.04])
        divider = mpl_toolkits.axes_grid1.make_axes_locatable(playerax)
        bax = divider.append_axes("right", size="80%", pad=0.05)
        sax = divider.append_axes("right", size="80%", pad=0.05)
        fax = divider.append_axes("right", size="80%", pad=0.05)
        ofax = divider.append_axes("right", size="100%", pad=0.05)
        self.button_oneback = matplotlib.widgets.Button(playerax, label=u'$\u29CF$')
        self.button_back = matplotlib.widgets.Button(bax, label=u'$\u25C0$')
        self.button_stop = matplotlib.widgets.Button(sax, label=u'$\u25A0$')
        self.button_forward = matplotlib.widgets.Button(fax, label=u'$\u25B6$')
        self.button_oneforward = matplotlib.widgets.Button(ofax, label=u'$\u29D0$')
        self.button_oneback.on_clicked(self.onebackward)
        self.button_back.on_clicked(self.backward)
        self.button_stop.on_clicked(self.stop)
        self.button_forward.on_clicked(self.forward)
        self.button_oneforward.on_clicked(self.oneforward)
