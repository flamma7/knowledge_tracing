import numpy as np
import matplotlib.pyplot as plt


start_prob = 0.99

c = 0.00005 # lose 0.2% per second
sim_time = 60 * 60 * 24 # 3 hours
arr = [0.99]
for t in range(sim_time):
    last_val = arr[-1]
    new_val = last_val * (1-c)
    arr.append(new_val)

plt.plot(arr)
plt.show()