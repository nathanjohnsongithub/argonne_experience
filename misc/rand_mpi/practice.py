
#execute with mpirun inp 4 python program.py
#4 is the number of processes you want to run
#comm.send(self, dest, tag)
'''
self - object containing the data to be sent
dest - rank of the process which is the destination for the message
tag  - number, which can be used to distinguish amound messages (good for debugging )
'''
#comm.recv(obj, source, tag)
'''
obj - object contatinig the data to be recievec
sources - rank of the proces from which to recive message
*this will completly stop the program until something is recieved
'''
#Get_rank(...)
'''
return the rank of this process in a communicator
'''
#Get_size(...)
'''
Return the number of processes in a communicator
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()

if my_rank != 0:
    message = "Hello from "+str(my_rank)
    comm.send(message, dest=0)
else :
    for procid in range(1,p):
        message = comm.recv(source=procid)
        print('hello from ',procid)
