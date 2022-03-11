import matplotlib.pyplot as plt
import numpy as np

x = np.array([35, 25, 25, 65, 55, 52, 46, 15])
lb = ["Apple", "Friiir", "jsfnl", "hjew", "ljfk", "sjf", "sjh", "sjf"]
myexplode = [0.2, 0, 0, 0 ,0 , 0, 0, 0]
my_colors = ["black", "hotpink", "darkred", "b", "r", "y", "brown", "m"]

plt.pie(x, labels = lb, startangle= 90, explode= myexplode, shadow = True, colors = my_colors)
plt.legend(title = "Random")
plt.show()
