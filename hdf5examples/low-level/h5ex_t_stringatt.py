"""
This example shows how to read and write string datatypes to a dataset.  The
program first writes strings to a dataset with a dataspace of DIM0, then
closes the file.  Next, it reopens the file, reads back the data, and outputs
it to the screen.

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

FILE = "h5ex_t_stringatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET = DATASET.encode()
    ATTRIBUTE = ATTRIBUTE.encode()

DIM0 = 4
SDIM = 8

def run():
    npdtype = '|S' + str(SDIM)
    wdata = np.empty((4,), npdtype)
    wdata[0] = "Parting"
    wdata[1] = "is such"
    wdata[2] = "sweet"
    wdata[3] = "sorrow"

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create the file and memory datatypes.  For this example we will save the
    # strings as FORTRAN strings, therefore they do not need space for the null
    # terminator in the file.
    filetype = h5py.h5t.FORTRAN_S1.copy()
    filetype.set_size(SDIM-1)
    memtype = h5py.h5t.C_S1.copy()
    memtype.set_size(SDIM)


    # Create a dataset with a scalar dataspace.
    # The origin C example uses a NULL dataspace, but this does not seem to
    # yet be possible in H5PY.
    space = h5py.h5s.create(h5py.h5s.SCALAR)
    dset = h5py.h5d.create(fid, DATASET, h5py.h5t.STD_I32LE, space)

    # Create the attribute dataspace.
    space = h5py.h5s.create_simple((DIM0,))

    # Create the attribute and write the string data to it.
    attr = h5py.h5a.create(dset, ATTRIBUTE, filetype, space)
    attr.write(wdata)

    # Explicitly close and release resources.
    del attr
    del space
    del dset
    del fid

    # Open file and dataset using the default properties.
    fid = h5py.h5f.open(FILE)
    dset = h5py.h5d.open(fid, DATASET)
    attr = h5py.h5a.open(dset, ATTRIBUTE)

    # Get the dataspace and allocate an array big enough to accomodate it.
    space = attr.get_space()
    dims = space.get_simple_extent_dims()

    rdata = np.empty(dims, dtype=npdtype)
    attr.read(rdata)

    # Output the data to the screen.
    print("%s:" % ATTRIBUTE)
    print(rdata)


if __name__ == "__main__":
    run()        
   

