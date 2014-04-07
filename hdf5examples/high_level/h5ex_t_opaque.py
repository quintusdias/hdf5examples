"""
This example shows how to read and write opaque datatypes to a dataset.
The program first writes opaque values to a dataset with a dataspace of DIM0,
then closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_opaque.h5"
DATASET = "DS1"

DIM0 = 4
LEN = 7

def run():

    # Initialize the data. Use the Numpy void datatype to stand in for
    # H5T_OPAQUE
    dtype=np.dtype('V7')
    wdata = np.zeros((DIM0,), dtype=dtype)
    for i in range(DIM0):
        wdata[i]= b'OPAQUE' + bytes([i + 48])

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0,), dtype=dtype)
        dset[...] = wdata

    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset[...]

    print("%s:" % DATASET)
    for row in rdata:
        print(row.tostring())


if __name__ == "__main__":
    run()        
   

