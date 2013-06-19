"""
This example shows how to read and write variable-length string datatypes to a
dataset.  The program first writes strings to a dataset with a dataspace of
DIM0, then closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.

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

FILE = "h5ex_t_vlstring.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET = DATASET.encode()
    ATTRIBUTE = "A1".encode()

DIM0 = 4

def run():
    # The "write" data must be a numpy array for variable length strings,
    # not a list.  
    #
    # Does this mean that we can use "|O"?
    wdata = np.empty((DIM0,), "|O")
    wdata[0] = "Parting"
    wdata[1] = "is such"
    wdata[2] = "sweet"
    wdata[3] = "sorrow"

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create the file and memory datatypes.  
    filetype = h5py.h5t.FORTRAN_S1.copy()
    filetype.set_size(h5py.h5t.VARIABLE)
    memtype = h5py.h5t.C_S1.copy()
    memtype.set_size(h5py.h5t.VARIABLE)

    # Create the dataspace.  No maximum size parameter needed.
    space = h5py.h5s.create_simple((DIM0,))

    # Create the dataset and write the string data to it.
    dset = h5py.h5d.create(fid, DATASET, filetype, space)
    dset.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)

    # Explicitly close and release resources.
    del space
    del dset
    del fid

    # Open file and dataset using the default properties.
    fid = h5py.h5f.open(FILE)
    dset = h5py.h5d.open(fid, DATASET)

    rdata = np.empty((DIM0,), dtype="|O")
    dset.read(h5py.h5s.ALL, h5py.h5s.ALL, rdata)

    # Output the data to the screen.
    print("%s:" % DATASET)
    print(rdata)


if __name__ == "__main__":
    run()        
   

