from pycbc import catalog
import matplotlib.pyplot as plt
import numpy as np

# Get data from the catalog about this event 
m = catalog.Merger('GW150914')

# look at the strain data from the Hanford site
h = m.strain('H1')
plt.plot(h.sample_times, h)
plt.title("Raw strain data for GW150914 H1")
plt.show()

# in terms of signal analysis, the first thing we want to do is whiten the data:
hw = h.whiten(4, 4) # 4 seconds of each sample used in PSD estimate, 4 second duration of filter

# still lots of high-frequency and low-frequency noise, so let's run
hf = hw.highpass_fir(30, 512)
hf = hf.lowpass_fir(250, 512)

plt.plot(hf.sample_times, hf)
plt.title("Whitened and filtered strain data for GW150914 H1")
plt.show()

# what's that around the middle?  Zoom in (we know the actual merger time, so use that)
hz = hf.time_slice(m.time - 0.5, m.time + 0.5)
plt.plot(hz.sample_times, hz)
plt.title("Zoomed in on the signal")
plt.show()
