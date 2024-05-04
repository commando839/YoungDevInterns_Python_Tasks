import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(0, 2 * np.pi, 100)  # from 0 to 2π

# Calculate y values for sine and cosine
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the sine and cosine curves with colorful lines
ax.plot(x, y_sin, label='Sine', color='tab:blue', linestyle='-', linewidth=2)
ax.plot(x, y_cos, label='Cosine', color='tab:red', linestyle='--', linewidth=2)

# Add a legend with a table
legend = ax.legend(loc='upper right', shadow=True, fontsize='large', fancybox=True)
legend.get_frame().set_facecolor('lightgrey')

# Set the title with 16 Bold Times New Roman font
ax.set_title('Sine and Cosine Graphs', fontsize=16, fontweight='bold', fontname='Times New Roman')

# Set the x and y axis labels and ticks
ax.set_xlabel('X-axis', fontsize=14)
ax.set_ylabel('Y-axis', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)

# Add grid lines for better readability
ax.grid(True, linestyle='--', linewidth=0.5)

# Show the plot plt.show()
plt.show()  
