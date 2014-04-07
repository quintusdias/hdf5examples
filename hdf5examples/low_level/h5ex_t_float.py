"""
This example shows how to read and write float datatypes to a dataset.  The
program first writes floats to a dataset with a dataspace of DIM0xDIM1, then
closes the file.  Next, it reopens the file, reads back the data, and outputs
it to the screen.
"""
import sys

import numpy as np
import h5py

FILE = "h5ex_t_float.h5"
DATASET = "DS1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET = DATASET.encode()

DIM0 = 4
DIM1 = 7

def run():
    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.float64)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i / (j + 0.5) + j

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create the dataspace.  No maximum size parameter needed.
    dims = (DIM0, DIM1)
    space = h5py.h5s.create_simple(dims)

    # Create the dataset and write the floating point data to it.  In this
    # example, we will save the data as 64 bit little endian IEEE floating
    # point numbers, regardless of the native type.  The HDF5 library
    # automatically converts between different floating point types.
    dset = h5py.h5d.create(fid, DATASET, h5py.h5t.IEEE_F64LE, space)
    dset.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)

    # Explicitly close and release resources.
    del space
    del dset
    del fid

    # Open file and dataset using the default properties.
    fid = h5py.h5f.open(FILE)
    dset = h5py.h5d.open(fid, DATASET)

    rdata = np.zeros((DIM0, DIM1), dtype=np.float64)
    dset.read(h5py.h5s.ALL, h5py.h5s.ALL, rdata)

    # Output the data to the screen.
    print("%s:" % DATASET)
    print(rdata)


if __name__ == "__main__":
    run()        
   

