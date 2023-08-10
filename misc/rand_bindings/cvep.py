import ctypes
import numpy as np

# Load the shared library
sum_vectors_lib = ctypes.CDLL('./sum_vectors.so')

# Define the function signature
sum_vectors_lib.sum_vectors.argtypes = (
    np.ctypeslib.ndpointer(dtype=np.int32),  # vec1
    np.ctypeslib.ndpointer(dtype=np.int32),  # vec2
    ctypes.c_int,                            # size
    np.ctypeslib.ndpointer(dtype=np.int32)   # result
)
sum_vectors_lib.sum_vectors.restype = None

vec1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int32)
vec2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int32)
size = len(vec1)

result = np.zeros((size,size), dtype=np.int32)

sum_vectors_lib.sum_vectors(vec1, vec2, size, result)

print("vector 1", vec1)
print("vector 2", vec2)

print("\nC++ Result:\n", result)

