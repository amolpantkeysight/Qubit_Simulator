import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Filter requirements.
order = 7
fs = 200*1000000       # sample rate, Hz
cutoff = 10*100000  # desired cutoff frequency of the filter, Hz

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()


# # Demonstrate the use of the filter.
# # First make some data to be filtered.
T = 5.0/400000         # seconds
n = int(T * fs) # total number of samples
t = np.linspace(0, T, n, endpoint=False)
# # "Noisy" data.  We want to recover the 1.2 Hz signal from this.
# data = np.sin(1.2**10000002*np.pi*t) + 1.5*np.cos(9*2*1000000*np.pi*t) + 0.5*np.sin(12.0**10000002*np.pi*t)
def func(x):
    return np.sin(1000000*x*np.pi)
    # return (np.sin(1000000 * np.pi * x/2000000)) * (np.cos(1000000 * np.pi * x/2000000))
data = np.sin(10000000*t*np.pi) + np.cos(2000000*t*np.pi)
#
# # Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(data, cutoff, fs, order)
#
plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
#
plt.subplots_adjust(hspace=0.35)
plt.show()
