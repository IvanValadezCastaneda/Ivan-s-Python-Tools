import numpy as np
import matplotlib.pyplot as plt


segment_1 = [(x1, y1), (x2, y2), ...]
segment_2 = [(x3, y3), (x4, y4), ...]

def fit_linear_segment(points):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    coefficients = np.polyfit(x, y, 1)  # Linear fit (degree 1)
    return np.poly1d(coefficients)


linear_eq_1 = fit_linear_segment(segment_1)
linear_eq_2 = fit_linear_segment(segment_2)
# Add more linear equations as needed


def GPStoImage(Latitude, Longitude):
    if condition_for_segment_1:  
        x_img = ...  
        y_img = linear_eq_1(x_img)
    elif condition_for_segment_2:  
        x_img = ... 
        y_img = linear_eq_2(x_img)

    adjusted_x = x_img + marginX
    adjusted_y = y_img + marginY

    FinalPosition = [adjusted_x, adjusted_y]
    return FinalPosition

plt.scatter(x, y, color='red')
plt.plot(x, linear_eq_1(x), color='blue')
plt.plot(x, linear_eq_2(x), color='green')
plt.xlabel('x (pixel)')
plt.ylabel('y (pixel)')
plt.title('Piecewise Linear Fit')
plt.gca().invert_yaxis()
plt.show()
