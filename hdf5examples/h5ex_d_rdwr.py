"""
This example shows how to read and write data to a dataset.  The
program first writes integers to a dataset with dataspace dimensions
of DIM0xDIM1, then closes the file.  Next, it reopens the file,
reads back the data, and outputs it to the screen.

Tested with:
    Fedora 18:
        HDF5 1.8.9, Python 2.7.3, Numpy 1.7.1, h5py 2.1.3
    Fedora 18:
        HDF5 1.8.9, Python 3.3.0, Numpy 1.7.1, h5py 2.1.3
    Mac OS X 10.6.8:
        HDF5 1.8.10, Python 3.2.5, Numpy 1.7.1, h5py 2.1.3
"""
import sys

import numpy as np
import h5py

FILE = "h5ex_d_rdwr.h5"
DATASET = "DS1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET = DATASET.encode()

DIM0 = 4
DIM1 = 7

def run():

    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i * j - j

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create the dataspace.  No maximum size parameter needed.
    dims = (DIM0, DIM1)
    space = h5py.h5s.create_simple(dims)

    # Create the datasets using default properties.
    dset = h5py.h5d.create(fid, DATASET, h5py.h5t.STD_I32LE, space)

    # Write the data to the dataset.
    dset.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)

    # Close and release resources.
    del dset
    del space
    del fid

    # Reopen the file and dataset using default properties.
    fid = h5py.h5f.open(FILE)
    dset = h5py.h5d.open(fid, DATASET)

    # Read the data using default properties.
    rdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    dset.read(h5py.h5s.ALL, h5py.h5s.ALL, rdata)

    print("%s:" % DATASET)
    print(rdata)

if __name__ == "__main__":
    run()        
