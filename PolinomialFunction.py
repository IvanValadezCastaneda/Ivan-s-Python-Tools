import numpy as np
import matplotlib.pyplot as plt

# Provided points
points = [
    (10, 435), (30, 427), (49, 417), (70, 408), (88, 402), (111, 393), (126, 383), (142, 379),
    (153, 374), (165, 369), (187, 358), (201, 352), (214, 344), (227, 340), (235, 336), (247, 330),
    (262, 326), (278, 318), (292, 313), (306, 305), (317, 301), (328, 295), (342, 289), (353, 284),
    (363, 280), (370, 274), (384, 269), (397, 264), (412, 257), (424, 254), (433, 251), (439, 247),
    (448, 243), (458, 242), (468, 238), (484, 231), (501, 231), (515, 228), (528, 224), (542, 222),
    (557, 220), (569, 217), (585, 211), (598, 211), (614, 208), (626, 205), (636, 202), (655, 198),
    (671, 194), (683, 190), (701, 188), (713, 186), (724, 183), (740, 180), (757, 176), (771, 172),
    (786, 169), (799, 164), (808, 162), (819, 162), (832, 161), (843, 159), (855, 155), (869, 154),
    (878, 151), (890, 148), (900, 146), (907, 150), (921, 150), (924, 150), (936, 150), (943, 150),
    (955, 146), (964, 145), (979, 144), (992, 138), (1005, 134), (1020, 134), (1034, 131), (1041, 128),
    (1051, 126), (1060, 125), (1070, 124), (1082, 119), (1096, 117), (1117, 116), (1123, 112),
    (1138, 109), (1151, 106), (1158, 102), (1173, 100), (1187, 97), (1198, 95), (1213, 95),
    (1227, 91), (1240, 88), (1251, 84), (1264, 78), (1271, 78)
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
