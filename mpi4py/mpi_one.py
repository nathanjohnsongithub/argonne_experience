from mpi4py import MPI

# Initialize mpi and get the rank and # of ranks (size)
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# All of the ranks print there ranks and the size
print('rank', rank, 'size',size)

# List with multiple colors
colors = ["white", "green", "orange", "blue"]

# the color for each respective rank is based on the value of there rank
color = colors[rank]

print(color)
