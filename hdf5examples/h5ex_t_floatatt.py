"""
This example shows how to read and write float datatypes to an attribute. The
program first writes floats to a dataset with a dataspace of DIM0xDIM1, then
closes the file.  Next, it reopens the file, reads back the data, and outputs
it to the screen.

Tested with:
    HDF5:   1.8.9/1.8.10
    Python: 2.7.3/3.2.3
    Numpy:  1.7.1/1.7.1
    H5PY:   2.1.0/2.1.2
"""
import sys

import numpy as np
import h5py

FILE = "h5ex_t_floatatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET = DATASET.encode()
    ATTRIBUTE = ATTRIBUTE.encode()

DIM0 = 4
DIM1 = 7
DIMS = (DIM0, DIM1)

def run():
    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.float64)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i / (j + 0.5) + j

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create a dataset with a scalar dataspace.
    # The origin C example uses a NULL dataspace, but this does not seem to
    # yet be possible in H5PY.
    space = h5py.h5s.create(h5py.h5s.SCALAR)
    dset = h5py.h5d.create(fid, DATASET, h5py.h5t.STD_I32LE, space)
    dset.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)
    del space

    # Create the attribute dataspace.  Not supplying a maximum size results
    # in the maximum size being equal to the current size.
    space = h5py.h5s.create_simple(DIMS)

    # Create the attribute and write the floating point data to it.
    # In this example we will save the data as 64 bit little endian
    # IEEE floating point numbers, regardless of the native type.  The
    # HDF5 library automatically converts between different floating point
    # types.
    attr = h5py.h5a.create(dset, ATTRIBUTE, h5py.h5t.IEEE_F64LE, space)
    attr.write(wdata)
            

    # Explicitly close and release resources.
    del attr
    del dset
    del space
    del fid

    # Open file and dataset using the default properties.
    fid = h5py.h5f.open(FILE)
    dset = h5py.h5d.open(fid, DATASET)
    attr = h5py.h5a.open(dset, ATTRIBUTE)

    # Get the dataspace and allocate space for the read buffer.
    space = attr.get_space()
    rdata = np.zeros((DIM0, DIM1), dtype=np.float64)

    attr.read(rdata)

    # Output the data to the screen.
    print("%s:" % ATTRIBUTE)
    print(rdata)


if __name__ == "__main__":
    run()        
   

