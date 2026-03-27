import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/radar_data.csv")
mix = data['mix'].values

fs = 1e6
num_chirps = 10
samples_per_chirp = len(mix) // num_chirps

mix_matrix = mix[:num_chirps*samples_per_chirp].reshape((num_chirps, samples_per_chirp))

range_fft = np.fft.fft(mix_matrix, axis=1)
range_fft = np.abs(range_fft)

doppler_fft = np.fft.fftshift(np.fft.fft(range_fft, axis=0), axes=0)
doppler_map = np.abs(doppler_fft)

plt.figure(figsize=(8,6))
plt.imshow(doppler_map, aspect='auto', extent=[0, samples_per_chirp, -num_chirps//2, num_chirps//2])
plt.xlabel("Range bins")
plt.ylabel("Doppler bins")
plt.title("Range-Doppler Map")
plt.colorbar(label="Amplitude")
plt.savefig("../images/range_doppler_map.png", dpi=150)
plt.show()
