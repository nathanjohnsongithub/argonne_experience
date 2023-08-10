import calculator
from py_rectangle_class import Rectangle
import numpy as np

arr = np.array([1,3,5,10])
print("Original:", arr)

changed_arr = calculator.multiply(arr)
print("Changed: ", changed_arr)


rec : Rectangle  = calculator.class_instance("paul", 8, 4)

print("\n[python]")
print(rec)
print("\n[python] Returned area:", rec.area(), "\n")
