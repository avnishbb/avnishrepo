import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 400)
y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="y = 2x + 1", color="blue")
plt.plot(x, y2, label="y = 2x + 2", color="green")
plt.plot(x, y3, label="y = 2x + 3", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lines y = 2x + 1, y = 2x + 2, y = 2x + 3")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
plt.grid(True)

# Display the plot
plt.show
