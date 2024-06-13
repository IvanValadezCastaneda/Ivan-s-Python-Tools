import numpy as np
import matplotlib.pyplot as plt

# Provided points
points = [

]

# Convert to numpy arrays
points = np.array(points)
x = points[:, 0]
y = points[:, 1]

# Invert the y-axis (assuming the image height is 720 pixels)
image_height = 720
y = image_height - y

# Fit a polynomial of degree 3 (you can adjust the degree based on your needs)
degree = 3
coefficients = np.polyfit(x, y, degree)

# Create the polynomial function
poly_function = np.poly1d(coefficients)

# Print the polynomial function
print("Polynomial coefficients:", coefficients)
print("Polynomial function:", poly_function)

# Plot to visualize
plt.scatter(x, y, color='red')
plt.plot(x, poly_function(x), color='blue')
plt.xlabel('x (pixel)')
plt.ylabel('y (pixel)')
plt.title('Fitted Polynomial Curve')
plt.show()
