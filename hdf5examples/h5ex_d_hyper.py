"""
This example shows how to read and write data to a dataset by
hyberslabs.  The program first writes integers in a hyperslab
selection to a dataset with dataspace dimensions of DIM0xDIM1, then
closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.  Finally it reads the data again using
a different hyperslab selection, and outputs the result to the
screen.

Tested with:
    HDF5:   1.8.9/1.8.10
    Python: 2.7.3/3.2.3
    Numpy:  1.7.1/1.7.1
    H5PY:   2.1.0/2.1.2
"""
import sys

import numpy as np
import h5py

FILE = "h5ex_d_hyper.h5"
DATASET = "DS1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET = DATASET.encode()

DIM0 = 6
DIM1 = 8

def run():

    # Initialize the data.
    wdata = np.ones((DIM0, DIM1), dtype=np.int32)

    # Print the data to the screen.
    print("Original Data:")
    print(wdata)

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create the dataspace.  No maximum size parameter needed.
    dims = (DIM0, DIM1)
    space = h5py.h5s.create_simple(dims)

    # Create the datasets using the dataset creation property list.
    dset = h5py.h5d.create(fid, DATASET, h5py.h5t.STD_I32LE, space)

    # Define and select the first part of the hyperslab selection.
    start = (0, 0)
    stride = (3, 3)
    count = (2, 3)
    block = (2, 2)
    space.select_hyperslab(start, count, stride, block)

    # Define and select the second part of the hyperslab selection, which is
    # subtracted from the first selection.
    block = (1, 1)
    space.select_hyperslab(start, count, stride, block, h5py.h5s.SELECT_NOTB)

    # Write the data to the dataset.
    dset.write(h5py.h5s.ALL, space, wdata)

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

    print("\nData as written to disk by hyperslabs:")
    print(rdata)

    # Define and select the hyperslab to use for reading.
    space = dset.get_space()
    start = (0, 1)
    stride = (4, 4)
    count = (2, 2)
    block = (2, 3)
    space.select_hyperslab(start, count, stride, block)

    # Read the data using the previously selected hyperslab.
    rdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    dset.read(h5py.h5s.ALL, space, rdata)

    print("\nData as read from disk by hyperslab:")
    print(rdata)

if __name__ == "__main__":
    run()        
