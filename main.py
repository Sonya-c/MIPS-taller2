from mpi4py import MPI

comm = MPI.COMM_WORLD

n = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = []

    for i in range(n):
        comm.send(i, dest=i)
        res = comm.recv()
        data.append(res)
    
    print(data)

base = comm.recv(source=0)
res = base**2
comm.send(res, 0)
