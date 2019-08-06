# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:31:13 2019
This script is designed to track the state of a qubit for a given drive signal
It will read in the phase and amplitude of a microwave drive that has been downconverted at the qubit frequency
@author: ccrocker
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from qutip import *
from qutip.ipynbtools import version_table
from SimDataGenerator import *
from bloch_sphering import Animate


q = Qobj([[1], [0]])     #initializes a qubit into the state 0

b = Bloch()              #initializes the Bloch sphere and defines how points look
b.point_marker = ["o"]
b.point_color = ["b"]
b.point_size = [25]

"""
Next we define a function that performs a rotation in the bloch sphere by an angle theta about an axis in the x-y plane at angle phi
"""
def r(theta, phi):
    return rz(phi)*rx(theta)*rz(-phi)

def rn(theta, phi, dphi, n): #Here we define a recursive function to track the evolution from a detuned signal
    if n==0:
        return r(theta, phi)
    else:
        return rn(theta,phi,dphi,n-1)*r(theta, phi + n*dphi)



#Generate some fake amp and phase data

simD1 = SimData(npoints=1000,detuning=0.002, amp=0.1, phase=np.pi/2)

"""
A function for rotating the qubit state based on a SimData object
"""

def rSim(sObj,InitialState): #Here we define a recursive function to track the evolution from a detuned signal
    state = np.array([InitialState])
    for i in range(sObj.npoints):
        state = np.append(state,[r(sObj.Amps[i],sObj.Phases[i])*state[-1]])
    return state

def rSimS(sObj,InitialState): #Here we define a recursive function to track the evolution from a detuned signal in the rotating frame of the signal itself
    state = np.array([InitialState])
    for i in range(sObj.npoints):
        state = np.append(state,[r(sObj.Amps[i],sObj.Phases[i])*state[-1]])
    for i in range(sObj.npoints):
        state[i+1]=rz(-sObj.Phases[i])*state[i+1]
    return state

a=rSim(simD1,q)

front_end = Animate(a)
front_end.animation()
