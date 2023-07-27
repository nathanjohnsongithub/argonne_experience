from mpi4py import MPI

# Initialize MPI and get the rank of each process and the # of ranks (size)
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

##################### ENTER SIZE OF ARRAY #########################
n = 50 
###################################################################    

def recieve():
    arr = comm.recv(None,0)    # each rank recieves there portion of the array
    for i in range(len(arr)):  # they then convert the array to whatever you want
        arr[i] += 100*rank
    
    return arr # and return it 


def split_number(number, divisor):
    quotient = number // divisor #get the quotient
    remainder = number % divisor #find the remander after divided by the divisor 

    parts = [0]*(divisor+1) #make a new array with size+1 length because we need a zero at the start

    for i in range(1, divisor+1): #loop through the array
        if(i < remainder+1): # if I is less than the remained plus one because were starting from 1 not zero
            parts[i] += 1    # we should add one to the parts array because we have some remainder
        parts[i] += parts[i-1] + quotient # make each element equal to itself plus the last one plus the quotient
    
    return parts


arr = [0] * n # make an empty array of size n

if(rank == 0): #if the process is the master
    print('empty arr',arr) #  print empty array
    for i in range(n):     #  populate array only for master
        arr[i] = i
    
    arr_with_distribution = split_number(n, size) #make a spliced array of the number of ranks + one for a zero at the start using the split number function

    for i in range(0,size):  #loop through all the ranks and send there section of the array
        arr_splice = arr[arr_with_distribution[i]: arr_with_distribution[i+1]]
        comm.send(arr_splice, dest=i)    

comm.send(recieve(), dest=0) #all of the ranks send there converted array back to the master

if(rank == 0):
    print('\noriginal ', arr) #master prints the original array
    for i in range(0,size):
        arr[arr_with_distribution[i]: arr_with_distribution[i+1]] = comm.recv(None, i) #then loops through and recieves each section of the converted array 

    print('\nconverted\n',arr) #print converted array

MPI.Finalize() # close MPI
