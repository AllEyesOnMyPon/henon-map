import matplotlib.pyplot as plt
import numpy as np
x0 = 0
y0 = 0
a = 1.4
b = 0.3
n = 10000

plt.figure(dpi=300)

data = [(0, x0, y0)]

for counter in range(1, n + 1):
    xn = 1 - a * data[counter - 1][1] ** 2 + data[counter - 1][2]
    yn = b * data[counter - 1][1]
    data.append((counter, xn, yn))
    plt.plot(data[counter][1], data[counter][2], 'o', color='black', alpha= .2, markersize= .1)

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
plt.xticks(np.arange(-1.5, 1.5, 0.2))  # Zakres X od -1.5 do 1.5, co 0.5
plt.yticks(np.arange(-0.5, 0.5, 0.1))  # Zakres Y od -0.5 do 0.5, co 0.2

plt.title("Henon Map") 
plt.xlabel("xn")
plt.ylabel("yn")
plt.show()

    

