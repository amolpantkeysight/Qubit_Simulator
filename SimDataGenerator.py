# -*- coding: utf-8 -*-
"""

This is a script to generate some sample amplitude and phase data
Created on Wed Jun 12 08:14:28 2019

@author: ccrocker
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from qutip import *
from qutip.ipynbtools import version_table


class SimData:
    def __init__(self, amp=0.1, phase=0, npoints=1000, detuning=0.1):
        self.amp = amp
        self.phase = phase
        self.npoints = npoints
        self.detuning = detuning
        self.Amps = np.array([self.amp for i in range(self.npoints)])
        self.Phases = np.array([self.phase + self.detuning*i for i in range(self.npoints)])
        self.RStep = np.array([rz(self.Phases[i])*rx(self.Amps[i])*rz(-self.Phases[i]) for i in range(self.npoints)])

    
class PulseData:
    def __init__(self, amp=1, phase=np.pi/2, npoints=1000, detuning=0, freq=0.03, width=100):
        self.amp = amp
        self.phase = phase
        self.npoints = npoints
        self.freq = freq
        self.width = width
        self.detuning = detuning
        self.Phases = np.array([self.phase + self.detuning*i for i in range(self.npoints)])
        self.Amps = np.array([self.amp/(self.width*np.sqrt(2*np.pi))*np.exp(-((self.npoints/2-i)/self.width)**2)*np.sin(2*np.pi*self.freq*i+self.phase) for i in range(self.npoints)])
        self.RStep = np.array([rz(self.Phases[i])*rx(self.Amps[i])*rz(-self.Phases[i]) for i in range(self.npoints)])
        
"""       
a = PulseData()

plt.plot(a.Amps)
np.savetxt('PulseWaveform.csv',a.Amps)
"""