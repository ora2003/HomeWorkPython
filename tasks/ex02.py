
import numpy as np

# Exercise 2 - Creating Arrays

# Question 1 - Black grayscale image

black_image = np.zeros((100, 200), dtype=np.uint8)

# Question 2 - White grayscale image

white_image = np.full((100, 200), 255, dtype=np.uint8)

# Question 3 - Red color image

color_image = np.full((100, 200, 3), 0, dtype=np.uint8)
color_image[:] = [255, 0, 0]

# Prediction: shape = (100, 200, 3)

print("Question 3:")
print("Prediction: (100, 200, 3)")
print("Result:", color_image.shape)

# Question 4 - Array properties

print("\nQuestion 4 - Black image:")
print("Prediction: shape=(100, 200), ndim=2, size=20000, nbytes=20000")
print("Shape:", black_image.shape)
print("Ndim:", black_image.ndim)
print("Size:", black_image.size)
print("Nbytes:", black_image.nbytes)

print("\nQuestion 4 - White image:")
print("Prediction: shape=(100, 200), ndim=2, size=20000, nbytes=20000")
print("Shape:", white_image.shape)
print("Ndim:", white_image.ndim)
print("Size:", white_image.size)
print("Nbytes:", white_image.nbytes)

print("\nQuestion 4 - Color image:")
print("Prediction: shape=(100, 200, 3), ndim=3, size=60000, nbytes=60000")
print("Shape:", color_image.shape)
print("Ndim:", color_image.ndim)
print("Size:", color_image.size)
print("Nbytes:", color_image.nbytes)

# Question 5 - Image memory size

# 1920 x 1080 color image
# Prediction: 1920 * 1080 * 3 = 6220800 bytes

large_image = np.zeros((1080, 1920, 3), dtype=np.uint8)

print("\nQuestion 5 - 1920x1080 image:")
print("Prediction: 6220800 bytes")
print("Result:", large_image.nbytes)

# 12 megapixel color image
# Prediction: 12000000 * 3 = 36000000 bytes

image_12mp = np.zeros((3000, 4000, 3), dtype=np.uint8)

print("\nQuestion 5 - 12 megapixel image:")
print("Prediction: 36000000 bytes")
print("Result:", image_12mp.nbytes)

# Question 6 - Array operations

b = np.arange(12).reshape(3, 4)

print("\nQuestion 6:")

# Prediction: 3 rows and 4 columns, numbers 0 to 11

print("\nPrediction for b:")
print("[[ 0  1  2  3]")
print(" [ 4  5  6  7]")
print(" [ 8  9 10 11]]")
print("Result:")
print(b)

# Prediction: sum of all numbers = 66

print("\nPrediction for b.sum(): 66")
print("Result:", b.sum())

# Prediction: sum of each column = [12 15 18 21]

print("\nPrediction for b.sum(axis=0): [12 15 18 21]")
print("Result:", b.sum(axis=0))

# Prediction: sum of each row = [6 22 38]

print("\nPrediction for b.sum(axis=1): [6 22 38]")
print("Result:", b.sum(axis=1))

# Prediction: both elements are 11

print("\nPrediction for b[2, 3], b[-1, -1]: 11 11")
print("Result:", b[2, 3], b[-1, -1])

# Explanation

# axis=0 calculates the sum of each column.
# axis=1 calculates the sum of each row.
