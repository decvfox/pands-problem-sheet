# plottask.py
# (i) Plot a histogram of a normal distribution of a 1000 values 
#       with a mean of 5 and standard deviation of 2
# (ii)  Plot the function h(x)=x^3 in the range [0, 10], 
#Author: Declan Fox
# ref https://www.w3schools.com/python/numpy/numpy_random_normal.asp
# ref https://www.w3schools.com/python/matplotlib_pyplot.asp

import numpy as np
import matplotlib.pyplot as plt

normo = np.random.normal(loc=5, scale=2, size=1000)
plt.hist(normo, color='#1ECBE1')

xpoints = np.array(range(1,10))
ypoints = xpoints * xpoints * xpoints

plt.plot(xpoints, ypoints, label = "Normal Dist")
plt.legend()
plt.plot(xpoints, ypoints, color='#C44B3B', label = "x cubed")
plt.title("random histogram & Plot of x cubed")
plt.xlabel("X")
plt.ylabel("h(x)=x^3")
plt.legend()
plt.show()
