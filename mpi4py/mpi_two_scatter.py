from mpi4py import MPI
import numpy as np
import math

# Initialize MPI and get the rank of each process and the # of ranks (size)
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

##################### ENTER SIZE OF ARRAY #########################
n = 85
###################################################################    

def make_matrix(arr, rows):
    # get the size of the columns rounding up from the size of the array and the # or ranks
    cols = math.ceil(len(arr) / size)

    # Add the extra Null values so its an equal matrix
    arr += [None] * (rows - len(arr) % rows)

    # create the matrix and populate it with values fror the array 
    matrix = [[arr[i * cols + j] for j in range(cols)] for i in range(rows)]

    return matrix

def flatten_matrix(matrix):
    # create a numpy matrix from the matrix we inputed so we can flatten it and convert it back into a list
    temp_matrix = np.array(matrix).flatten().tolist()
      
    # find out how many Nones we need to remove
    for index, num in enumerate(reversed(temp_matrix)):
        if num is not None:
            break

    # return the new flattened matrix with the None values removed and check if any were removed so we dont accidently return an empty list
    return temp_matrix[:-index] if index != 0 else temp_matrix


# make an empty array of size n
arr = [0] * n 

# if the process is the master
if(rank == 0): 
    #  populate array only for master
    for i in range(n):     
        arr[i] = i
    
    # Get the matrix
    matrix = make_matrix(arr, size)
    # Print it out
    print("Matrix we will be scattering\n", matrix, "\n")
else:
    # Make the matrix equal to nothing for all other ranks (temporary)
    matrix = None

# Scatter the array to all the ranks equally
matrix = comm.scatter(sendobj=matrix, root=0)

# Each rank prints out there section they recieved
print(f"rank {rank}: has this section: {matrix}")

# Each rank adds 100 times there rank to the value of the matrix
matrix = [value + 100 * rank if value is not None else None for value in matrix]

# gather the now converted matrix 
converted_matrix = comm.gather(matrix, 0)

# Master prints out the converted matrix
if rank == 0:
    # flatten the matrix
    # NOTE Could just have everything as a numpy array as theyre better but I didnt want to change the list comprehension so we've got this
    converted_matrix = flatten_matrix(converted_matrix)
    print("\nConverted Matrix\n", converted_matrix)
    

MPI.Finalize() # close MPI
