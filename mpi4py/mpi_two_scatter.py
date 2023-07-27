from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#####################ENTER SIZE OF ARRAY#########################
n = 16
#################################################################    

def recieve():
    arr = comm.recv(None,0)    # each rank recieves there portion of the array
    print(rank, 'recieved', arr)
    for i in range(len(arr)):  # they then convert the array to whatever you want
        arr[i] += 100*rank
    
    return arr # and return it 

 # make an empty array of size 
def split_list(lst, n):

    length = len(lst)
    split_size = length // n  # Calculate the split size
    print(split_size)
    remainder = length%n
    forgotten = [0]*remainder
    j = 0
    for i in range(length-remainder,length):
        forgotten[j] = lst[i]
        if(j < remainder):
            j += 1
        else:
            break

    result = [lst[i:i + split_size] for i in range(0, n*split_size, split_size)]
    
    return result 


if(rank == 0): #if the process is the master
    arr = [0] * n
    print('empty arr',arr) #  print empty array
    for i in range(n):     #  populate array only for master
        arr[i] = i
    
    #arr = split_list(arr, size)
    print(arr)
else:
    arr = None
    
    #arr_with_distribution = split_number(n, size) #make a spliced array of the number of ranks + one for a zero at the start using the split number function

arr = comm.scatter(sendobj=arr, root=0)

print('I am rank',rank, 'i got', arr)

'''
comm.send(recieve(), dest=0) #all of the ranks send there converted array back to the master

if(rank == 0):
    print('\noriginal ', arr) #master prints the original array
    for i in range(0,size):
        arr[arr_with_distribution[i]: arr_with_distribution[i+1]] = comm.recv(None, i) #then loops through and recieves each section of the converted array 

    print('\nconverted\n',arr) #print converted array

MPI.Finalize() # close MPI
'''
