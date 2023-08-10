from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print('rank', rank)
print ('size',size)

color = 'black'

if(rank == 0):
    color = 'white'
elif(rank == 1):
    color = 'green'
elif(rank == 2):
    color = 'orange'
elif(rank == 3):
    color = 'blue'

if (comm.Get_rank() == 2):
    print(color)
