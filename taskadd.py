from mpi4py import MPI
import numpy as np
import time

time.sleep(5)

comm = MPI.COMM_WORLD
myrank = comm.Get_rank()
nproc = comm.Get_size()
N = 1000000
startval = int(N*myrank/nproc + 1)
endval = int(N*(myrank+1)/nproc)
partial_sum = np.array(0, dtype='i')

for i in range(startval, endval+1):
    partial_sum += i

tot_sum = np.array(0, dtype='i')
comm.Reduce([partial_sum, 1, MPI.INT],[tot_sum, 1, MPI.INT], op=MPI.SUM, root=0)
if (myrank == 0):
    print("The sum is {0}\n".format(tot_sum))

with open("./results/sum.txt", "w") as f:
    f.write(str(tot_sum))
    f.close()