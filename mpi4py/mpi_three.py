from mpi4py import MPI
import cProfile, sys

# initialize Mpi and get the rank of everyone and the # of ranks(size)
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def recieve():
    # recieve the array from the master
    arr = comm.recv(None,0)  
    # change the arr into the value of the rank doing it 
    arr = [rank for _ in arr]
    return arr 


def split_number(number, divisor):
    # get the quotient and the remainder
    quotient = number // divisor 
    remainder = number % divisor 

    # make the parts array equal to the size of the divisor also known as the # of ranks
    parts = [0]*(divisor) 

    for i in range(divisor): 
        # if there is still a remainder
        if(i < remainder):
            # add the remainder
            parts[i] += 1    
        # add on the last value to the current value plus the quotient
        # e.g. number = 50, divisor = 4. parts[1] = 12 + 0 + 12.
        parts[i] += parts[i-1] + quotient 
    
    return parts

def make_file():
    if(rank == 0):
        # open the file
        f = open('myfile1.txt', 'w+')   

        # make the string and the list
        s = ''
        lst = []

        for i in range(n):
            s += str(i) + '\n'
            lst.append(i)

        f.write(s) 
        f.close()
        
        # call the split_number function to get an array with the distribution of the splice for each rank
        arr_with_distribution = split_number(n, size)
        
        # loop through all the ranks and send there section of the array
        for i in range(0,size-1):  
            # section of the array to get sent
            arr_splice = lst[arr_with_distribution[i]: arr_with_distribution[i+1]]
            # send the section of the array
            comm.send(arr_splice, dest=i+1)    
            
        # change the values of the array for the master
        for i in range(arr_with_distribution[0]):   
            lst[i] = rank
    else:
        # send back the changed array to the master
        comm.send(recieve(), dest=0) #all of the ranks send there converted array back to the master

    if(rank == 0):
        # the master returns the arr_with_distribution and the lst
        return arr_with_distribution, lst
    
def upload(lst):
    # create the changed file
    fchanged = open('mychangedfile1.txt', 'w')
        
    for i in range(n):
        # write the values to the new file
        fchanged.write(str(lst[i]) + '\n')
    
    # close the file
    fchanged.close()

def recieve_and_populate(arr_with_distribution, lst):
    # loop through and recieve the array and put it into the lst
    for i in range(0,size-1):
        lst[arr_with_distribution[i]: arr_with_distribution[i+1]] = comm.recv(None, i+1) #then loops through and recieves each section of the converted array 

    upload(lst)
    

# create instance of the profiles
pr = cProfile.Profile()
# start profiling
pr.enable()
if __name__ == "__main__":
    if rank == 0:
        # Only master takes in the input otherwise it would print prompt X amount of times where X is the # of ranks
        n = int(input("Enter a integer number for the size of the array: "))
    else:
        # need to make "n" None for everybody so bcast works
        n = None

    # broadcast the value of n to everybody else from the "root" 0 or the master 
    n = comm.bcast(n, 0)

    result = make_file()
    if(rank == 0):
        recieve_and_populate(result[0], result[1])

# end profiling
pr.disable()    

# Dump results:
# - for binary dump
pr.dump_stats('cpu_%d.prof' %comm.rank)
# - for text dump
with open( 'cpu_%d.txt' %comm.rank, 'w') as output_file:
    sys.stdout = output_file
    pr.print_stats( sort='tottime' )
    sys.stdout = sys.__stdout__


# Close MPI
# NOTE not needed as initializing will automatically add this. 
MPI.Finalize() 