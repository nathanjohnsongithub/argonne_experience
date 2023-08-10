import numpy as np
import example

# Create two numpy arrays/vectors
vec1 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
vec2 = np.array([4.0, 5.0, 6.0, 7.0], dtype=np.float64)

# Call the C++ function and get the sum vector
sum_vec = example.sum_vectors(vec1, vec2)

# Print the result
print(sum_vec)
