import matplotlib.pyplot as plt
import numpy as np
import scipy
import os

wav_directory = "doppler_data_day2"

fs, data = scipy.io.wavfile.read(os.path.join(wav_directory, f'Day_2-Test_Trial_1.wav'))
func, t, Sxx = scipy.signal.spectrogram(data, fs, nperseg=2048, noverlap=1024, nfft=2**15, detrend='linear')
Sxx = 10 * np.log10(Sxx[0:400])
func = func[:400]

def label_path_on_spectrogram(Sxx, t, f):
    plt.figure(figsize=(12, 6))
    plt.imshow(Sxx, aspect='auto', origin='lower',
               extent=[t[0], t[-1], f[0], f[-1]],
               cmap='viridis')
    plt.title("Click on path points (press Enter when done)")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")

    # Use ginput to get (x, y) clicks from user
    points = plt.ginput(n=-1, timeout=0)  # -1 means unlimited points
    plt.close()

    print(points)

    # print as list of (time, freq)
    return points


# Usage
labels = label_path_on_spectrogram(Sxx, t, func)
