"""
This example shows how to read and write data to a dataset.  The
program first writes integers to a dataset with dataspace dimensions
of DIM0xDIM1, then closes the file.  Next, it reopens the file,
reads back the data, and outputs it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_d_rdwr.h5"
DATASET = "DS1"

DIM0 = 4
DIM1 = 7

def run():

    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i * j - j


    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0, DIM1), dtype='<i4')
        dset[...] = wdata


    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = np.zeros((DIM0, DIM1), dtype=np.int32)
        dset.read_direct(rdata)

    print("%s:" % DATASET)
    print(rdata)

if __name__ == "__main__":
    run()        
