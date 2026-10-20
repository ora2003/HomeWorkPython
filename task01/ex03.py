
import numpy as np

# Exercise 3 - Overflow

x = np.array([100, 200, 250], dtype=np.uint8)

# ------------------------------------------
# Question 1 - Predictions and results

# Prediction: Add 10 to every value
print("Prediction: Add 10 to every value")
print("Result:", x + 10)

# Prediction: Add 100 to every value
print("\nPrediction: Add 100 to every value")
print("Result:", x + 100)

# Prediction: Subtract 150 from every value
print("\nPrediction: Subtract 150 from every value")
print("Result:", x - 150)

# Prediction: Multiply every value by 2
print("\nPrediction: Multiply every value by 2")
print("Result:", x * 2)

# Prediction: Convert to 16-bit integers (2 bytes)
# and add 100 to every value
print("\nPrediction: Convert to int16 and add 100")
print("Result:", x.astype(np.int16) + 100)

# Prediction: Multiply every value by 1.5
print("\nPrediction: Multiply every value by 1.5")
print("Result:", x * 1.5)

# Prediction: Unknown
print("\nPrediction: Unknown dtype")
print("Result:", (x * 1.5).dtype)

# ------------------------------------------
# Question 2 - Overflow with 300

# Prediction: Overflow
try:
    print(x + 300)
except OverflowError as e:
    print("OverflowError:", e)

# Explanation:
# NumPy raises an OverflowError because 300
# cannot be represented as a uint8 scalar.
# The maximum value of uint8 is 255.

# ------------------------------------------
# Question 3 - Safe Addition

def add_safe(x, b):
    x = x.astype(np.int16)
    x = x + b
    x = np.clip(x, 0, 255)
    return x.astype(np.uint8)

print("b = 100:", add_safe(x, 100))
print("b = -150:", add_safe(x, -150))

# Explanation:
# b=100: Values above 255 are limited to 255.
# b=-150: Negative values are limited to 0.

# ------------------------------------------
# Question 4 - Explanation

# Overflow happens during x + 100, before np.clip is applied.
# Some values exceed 255 and wrap around because x is uint8.
# np.clip cannot fix the values after overflow.
# Therefore, we must convert x to int16 before adding 100.

# ------------------------------------------
# Question 5 - Bonus

# int8 range: -128 to 127
# Prediction: 127 + 1 = -128

x_int8 = np.array([127], dtype=np.int8)

print("Prediction: -128")
print("Result:", (x_int8 + 1))

# Explanation:
# int8 stores values from -128 to 127.
# When 127 + 1 is calculated, overflow occurs.
# The result wraps around to -128.
