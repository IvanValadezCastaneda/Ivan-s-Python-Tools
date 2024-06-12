import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread

# Load the image
img = imread(image_path)

# Display the image
fig, ax = plt.subplots()
ax.imshow(img)

# Click event handler to capture the points
points = []

def onclick(event):
    if event.xdata and event.ydata:
        x, y = int(event.xdata), int(event.ydata)
        points.append((x, y))
        ax.plot(x, y, 'ro')  # Plot red dots
        plt.draw()

# Connect the click event to the handler
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

# After closing the plot window, print the collected points
print("Collected points:", points)

# Save the points to a file or use them as needed
np.savetxt('points.txt', points, fmt='%d')
