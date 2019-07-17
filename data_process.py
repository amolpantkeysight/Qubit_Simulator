'''
Version: 1.0
07.12.2019
Uses waveform data stored from the oscilloscope as a .csv file and converts waveform to a 1-D array for values over a constant time step.
Uses the data array to process the signal to create animation on the bloch sphere.
Also starts up the animation process of the qubit.
Author: @Amol Pant
'''
from qutip import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from bloch_sphering import Animate
import csv
import os
import sys

#Opens data.csv file generated by the UDA and stores it as an array in 2D.
with open('C:\\Users\\amolpant\\Documents\\ScopeDataRetrieval\\data.csv', newline='') as csvfile:
    data_two = list(csv.reader(csvfile))

#Converts array from 2D to 1D.
data = data_two[0]

#Intermediate step to write data onto a .txt file named 'out'.
with open('C:\\Users\\amolpant\\Documents\\ScopeDataRetrieval\\out', 'w+') as f:
    for item in data:
        f.write("%s\n" % item)

# print(type(data[0]))

front_end = Animate(data)

front_end.animation()