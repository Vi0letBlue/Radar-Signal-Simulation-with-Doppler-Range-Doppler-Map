import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/radar_data.csv")

plt.figure()
plt.plot(data["time"], data["tx"], label="TX")
plt.plot(data["time"], data["rx"], label="RX")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Radar Signals")
plt.legend()
plt.savefig("../images/tx_rx_plot.png", dpi=150)
plt.show()
