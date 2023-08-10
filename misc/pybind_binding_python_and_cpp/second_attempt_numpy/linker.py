import calculator
import numpy as np

arr = np.array([1,3,5,10])

print("Original:", arr)

changed_arr = calculator.multiply(arr)

print("Changed: ", changed_arr)