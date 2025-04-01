import matplotlib.pyplot as plt
import numpy as np

# Henon Map parametry
# x_{n+1} = 1 - a * x_n^2 + y_n
x0, y0 = 0, 0 # start values
a, b = 1.4, 0.3 # Henon Map parameters a = 1.4, b = 0.3 (typical values)
n = 10000 # ieration count


x_vals, y_vals = [x0], [y0] # lists to store x and y values


for _ in range(n): # iterating n times to generate points on the Henon map
    xn = 1 - a * x_vals[-1]**2 + y_vals[-1] # Henon map equation for x
    yn = b * x_vals[-1] # Henon map equation for y
    x_vals.append(xn) # append new x value to the list
    y_vals.append(yn)   # append new y value to the list

plt.figure(dpi=300) # set the figure resolution to 300 dpi
plt.scatter(x_vals, y_vals, s=0.1, color="black", alpha=0.2) # plot the points with small size and low opacity

plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6) # add grid with dashed lines
plt.xticks(np.arange(-1.5, 1.6, 0.5)) # set x ticks from -1.5 to 1.5 with step 0.5
plt.yticks(np.arange(-0.5, 0.6, 0.2)) # set y ticks from -0.5 to 0.5 with step 0.2

plt.title("Henon Map") # set the title of the plot
plt.xlabel("xn") # set the x-axis label
plt.ylabel("yn") # set the y-axis label

plt.show()

    

