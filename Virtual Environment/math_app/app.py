import numpy as np
import matplotlib.pyplot as plt

print ("Random numbers: ", np.random.randint(1, 100, 5))

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.show()