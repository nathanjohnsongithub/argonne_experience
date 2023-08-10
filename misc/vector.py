import numpy as np

arr1 = np.array([0,1,2,3,4,5,6,7,8,9])
arr2 = np.array([0,1,2,3,4,5,6,7,8,9])

matrix = np.zeros((len(arr1),len(arr2)),int)

print(matrix)

for i in range(len(arr1)):
    for j in range(len(arr2)):
        matrix[i, j] = arr1[i] * arr2[j]

print(matrix)
