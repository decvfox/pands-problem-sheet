# plottask.py
# (i) Plot a histogram of a normal distribution of a 1000 values 
#       with a mean of 5 and standard deviation of 2
# (ii)  Plot the function h(x)=x^3 in the range [0, 10], 
#Author: Declan Fox
# ref https://www.w3schools.com/python/numpy/numpy_random_normal.asp
# ref https://www.w3schools.com/python/matplotlib_pyplot.asp

import numpy as np
import matplotlib.pyplot as plt

# Array of 1,000 elements as specified by the task
normo = np.random.normal(loc=5, scale=2, size=1000)

# plot a histogram of occurrences of each number in normo
plt.hist(normo, color='#1ECBE1', label = "Normal Dist")
plt.legend()

# create an array of numbers from 0 to 10
xpoints = np.array(range(0,11))
# create an array with all the elements of x points cubed
ypoints = xpoints * xpoints * xpoints

# plot each element of the 2 arrays
plt.plot(xpoints, ypoints, color='#C44B3B', label = "h(x)=x^3")
plt.legend()

# add a title and label the x and y axis
plt.title("Histogram of Normal Distribution & Plot of X Cubed")
plt.xlabel("x")
plt.ylabel("h(x)=x^3")

# draw the plot on screen
plt.show()
