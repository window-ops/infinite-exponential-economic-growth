import matplotlib.pyplot as plt
import numpy as np


# Define the function for exponential growth
def exponential_growth(x, a, b):
    return a * np.exp(b * x)


# Define the initial conditions for the exponential growth
a = 10  # economy
b = 0.3  # growth factor

# Define the maximum sustainable economic growth
max_growth = 3000


# Define a function to update the plot when the view changes
def update_plot(ax):
    xlim = ax.get_xlim()
    x = np.linspace(xlim[0], xlim[1], 1000)
    y = exponential_growth(x, a, b)
    line.set_data(x, y)
    ax.figure.canvas.draw()


# Create the initial plot
fig, ax = plt.subplots()
x = np.linspace(0, 10, 1000)
y = exponential_growth(x, a, b)
line, = ax.plot(x, y, linewidth=2, label='Economic Growth')

# Add a horizontal line to indicate the overshoot line
ax.axhline(y=max_growth, color='r', linestyle='--', label='Overshoot Line')

# Set the x and y-axis labels
ax.set_xlabel('Time')
ax.set_ylabel('Economic Growth')

# Set the plot title
ax.set_title('Infinite Exponential Economic Growth')

# Add a legend to the plot
ax.legend()

# Connect the update function to the plot's xlim_changed event
ax.callbacks.connect('xlim_changed', update_plot)

# Show the plot
plt.show()
