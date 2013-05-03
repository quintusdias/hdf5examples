"""
This example shows how to create and extend an unlimited dataset.
The program first writes integers to a dataset with dataspace
dimensions of DIM0xDIM1, then closes the file.  Next, it reopens
the file, reads back the data, outputs it to the screen, extends
the dataset, and writes new data to the entire extended dataset.
Finally it reopens the file again, reads back the data, and utputs
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

FILE = "h5ex_d_unlimmod.h5"
DATASET = "DS1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET = DATASET.encode()

DIM0 = 4
DIM1 = 7
EDIM0 = 6
EDIM1 = 10
CHUNK0 = 4
CHUNK1 = 4

def run():

    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i * j - j

    # Create a new file using the default properties.
    file = h5py.h5f.create(FILE)

    # Create the dataspace.  
    dims = (DIM0, DIM1)
    maxdims = (h5py.h5s.UNLIMITED, h5py.h5s.UNLIMITED)
    space = h5py.h5s.create_simple(dims, maxdims)

    # Create the dataset creation property list and set the chunk size.
    dcpl = h5py.h5p.create(h5py.h5p.DATASET_CREATE)
    chunk = (CHUNK0, CHUNK1)
    dcpl.set_chunk(chunk)

    # Create the chunked dataset.
    dset = h5py.h5d.create(file, DATASET, h5py.h5t.STD_I32LE, space, dcpl)

    # Write the data to the dataset.
    dset.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)

    # Close and release resources.
    del dcpl
    del dset
    del space
    del file

    # Now we begin the read section of this example.
    # Open the file and dataset.
    file = h5py.h5f.open(FILE, h5py.h5f.ACC_RDWR)
    dset = h5py.h5d.open(file, DATASET)

    # Get the dataspace and allocate an array for reading.  Numpy makes this
    # MUCH easier than C.
    space = dset.get_space()
    dims = space.get_simple_extent_dims()
    rdata = np.zeros(dims, dtype=np.int32)

    # Read the data using the default properties.
    dset.read(h5py.h5s.ALL, h5py.h5s.ALL, rdata)
    print("Dataset before extension:")
    print(rdata)

    # Extend the dataset.
    extdims = (EDIM0, EDIM1)
    dset.set_extent(extdims)

    # Initialize data for writing to the extended dataset.
    wdata = np.zeros((EDIM0, EDIM1), dtype=np.int32)
    for i in range(EDIM0):
        for j in range(EDIM1):
            wdata[i][j] = j

    # Write to the extended dataset.
    dset.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)

    # Close and release resources.
    del dset
    del space
    del file

    # Now simply read back the data and echo to the screen.
    file = h5py.h5f.open(FILE)
    dset = h5py.h5d.open(file, DATASET)

    # Get the dataspace and allocate an array for reading.
    space = dset.get_space()
    dims = space.get_simple_extent_dims()
    rdata = np.zeros(dims, dtype=np.int32)

    # Read the data using the default properties.
    dset.read(h5py.h5s.ALL, h5py.h5s.ALL, rdata)
    print("Dataset after extension:")
    print(rdata)

    # Close and release resources.
    del dset
    del space
    del file


if __name__ == "__main__":
    run()
