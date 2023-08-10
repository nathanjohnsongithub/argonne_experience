'''
Master has an empty array and prints all of it 

then populate array and send to each section split into 4
100/4

each section does there own operations of the array and the master reciveves is 

master prints the original array then the array that it reciecved with all of the adusted values 
'''
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def recieve():
    arr = comm.recv(None,0)
    #print('rank', rank, 'recieved ',arr,'\n')
    for i in range(len(arr)):
        arr[i] = 10 + rank
    #print('changed array',arr,'\n')
    return arr   

arr = []

#make array with 20*size elements all being 0
for i in range(20*(size)):
    arr.append(0)

#populate array only for master
if(rank == 0): 
    #print empty array
    print('empty arr',arr)
    for i in range(20*(size)):
        arr[i] = i
    #print(arr)
    #loop through all the other ranks and send the spliced array
    for i in range(0,size):
        arr_splice = arr[20*i: 20*(i+1)]
        #print('array',i ,arr_splice)
        comm.send(arr_splice, dest=i)    

comm.send(recieve(), dest=0)
if(rank == 0):
    print('\noriginal ', arr)
    for i in range(0,size):
        arr[20*i: 20*(i+1)] = comm.recv(None, i)
    print('\nconverted',arr)

MPI.Finalize()

    
