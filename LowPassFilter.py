import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import math

class DownConversion():

    def __init__(self, signal_data, sampling_rate, cuttoff_freq, window_size, time):
        self.data = signal_data
        self.fs = sampling_rate
        self.cutoff = cuttoff_freq
        self.order = window_size
        self.T = time

    def decompose(self):

        # Get the filter coefficients so we can check its frequency response.
        def butter_lowpass(cutoff, fs, order=5):
            nyq = 0.5 * fs
            normal_cutoff = cutoff / nyq
            b, a = butter(order, normal_cutoff, btype='low', analog=False)
            return b, a

        def butter_lowpass_filter(data, cutoff, fs, order=5):
            b, a = butter_lowpass(cutoff, fs, order=order)
            y = lfilter(b, a, data)
            return y

        b, a = butter_lowpass(self.cutoff, self.fs, self.order)

        print(len(b))
        print(len(a))

        w, h = freqz(b, a, worN=8000)
        # plt.subplot(2, 1, 1)
        # plt.plot(0.5*self.fs*w/np.pi, np.abs(h), 'b')
        # plt.plot(self.cutoff, 0.5*np.sqrt(2), 'ko')
        # plt.axvline(self.cutoff, color='k')
        # plt.xlim(0, 0.5*self.fs)
        # plt.title("Lowpass Filter Frequency Response")
        # plt.xlabel('Frequency [Hz]')
        # plt.grid()
        n = int(self.T * self.fs) # total number of samples
        t = np.linspace(0, self.T, n, endpoint=False)

        # self.data = np.sin(1000000000*t*np.pi) + np.cos(200000000*t*np.pi)

        data_i = self.data * np.sin(30000000*t*2*np.pi)
        data_q = self.data * np.cos(30000000*t*2*np.pi)

        y = butter_lowpass_filter(data_i, self.cutoff, self.fs, self.order)
        z = butter_lowpass_filter(data_q, self.cutoff, self.fs, self.order)


        #Plotting Stuff
        # plt.subplot(2, 1, 2)
        # plt.plot(t, self.data, 'b-', label='data')
        # plt.plot(t, data_i, 'r-', label='I')
        # plt.plot(t, data_q, 'g-', label='Q')
        # plt.xlabel('Time [sec]')
        # plt.grid()
        # plt.legend()
        #
        # plt.subplot(2,2,1)
        # plt.plot(t, y, 'g-', linewidth=2, label='filtered data_I')
        # plt.plot(t, z, 'y-', linewidth=2, label='filtered data_Q')
        # plt.xlabel('Time [sec]')
        # plt.grid()
        # plt.legend()
        # #
        # plt.subplot(2,2,2)
        # amp = np.zeros(len(self.data))
        # phases = np.zeros(len(self.data))
        # for i in range(len(data_i)-1):
        #     amp[i] = math.sqrt(data_i[i]**2 + data_q[i]**2)
        #     phases[i] = math.atan(data_q[i]/data_i[i])
        # plt.plot(t, amp, 'b-', label='Amplitude')
        # plt.plot(t, phases, 'r-', label='Phase')
        # plt.xlabel('Time [sec]')
        # plt.grid()
        # plt.legend()
        # plt.subplots_adjust(hspace=0.35)
        # plt.show()

        return amp, phases
