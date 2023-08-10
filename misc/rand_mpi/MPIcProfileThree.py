from mpi4py import MPI
from mpi4py.MPI import COMM_WORLD
import cProfile, sys



comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


#######################
n = 10000000
#######################

def recieve():
    arr = comm.recv(None,0)   
    for i in range(len(arr)):   
        arr[i] = rank
    
    return arr 


def split_number(number, divisor):
    quotient = number // divisor 
    remainder = number % divisor 

    parts = [0]*(divisor) 

    for i in range(divisor): 
        if(i < remainder):
            parts[i] += 1    
        parts[i] += parts[i-1] + quotient 
    
    return parts

def make_file():
    if(rank == 0):
        f = open('myfile1.txt', 'w+')   # open file

        s = ''

        for i in range(n):
            s += str(i) + '\n'

        f.write(s) 

        f.seek(0)
        lst = [int(x) for x in f.read().split()]
        f.close()
        
        arr_with_distribution = split_number(n, size)
        
        for i in range(0,size-1):  #loop through all the ranks and send there section of the array
            arr_splice = lst[arr_with_distribution[i]: arr_with_distribution[i+1]] # [1250, 2500, 3750, 5000]
            comm.send(arr_splice, dest=i+1)    
            

        for i in range(arr_with_distribution[0]):   
            lst[i] = rank
    else:
        comm.send(recieve(), dest=0) #all of the ranks send there converted array back to the master

    if(rank == 0):
        return arr_with_distribution, lst
    
def upload(lst):
    fchanged = open('mychangedfile1.txt', 'w')
        
    for i in range(n):
        fchanged.write(str(lst[i]) + '\n')
    
    fchanged.close()

def recieve_and_populate(arr_with_distribution, lst):
    for i in range(0,size-1):
        lst[arr_with_distribution[i]: arr_with_distribution[i+1]] = comm.recv(None, i+1) #then loops through and recieves each section of the converted array 

    upload(lst)
    


pr = cProfile.Profile()
pr.enable()
if __name__ == "__main__":
    result = make_file()
    if(rank == 0):
        recieve_and_populate(arr_with_distribution=result[0], lst=result[1])
pr.disable()    

# Dump results:
# - for binary dump
pr.dump_stats('cpu_%d.prof' %comm.rank)
# - for text dump
with open( 'cpu_%d.txt' %comm.rank, 'w') as output_file:
    sys.stdout = output_file
    pr.print_stats( sort='tottime' )
    sys.stdout = sys.__stdout__


MPI.Finalize() # close MPI
