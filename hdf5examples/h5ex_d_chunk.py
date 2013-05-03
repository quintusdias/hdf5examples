"""
This example shows how to create a chunked dataset.  The program first writes
integers in a hyperslab selection to a chunked dataset with dataspace
dimensions of DIM0xDIM1 and chunk size of CHUNK0xCHUNK1, then closes the file.
Next, it reopens the file, reads back the data, and outputs it to the screen.
Finally it reads the data again using a different hyperslab selection, and
outputs the result to the screen.

Tested with:
    HDF5:   1.8.9/1.8.10
    Python: 2.7.3/3.2.3
    Numpy:  1.7.1/1.7.1
    H5PY:   2.1.0/2.1.2
"""
import sys

import numpy as np
import h5py

FILE = "h5ex_d_chunk.h5"
DATASET = "DS1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET.encode()

DIM0 = 6
DIM1 = 8
dims = (DIM0, DIM1)
CHUNK0 = 4
CHUNK1 = 4
chunk = (CHUNK0, CHUNK1)

def run():
    # Initialize data to 1 to make it easier to see the selections.
    wdata = np.ones((DIM0, DIM1))
    print(wdata)

    # Create a new file using the default properties.
    file = h5py.h5f.create(FILE)

    # Create the dataspace.  
    space = h5py.h5s.create_simple(dims, None)

    # Create the dataset creation property list and set the chunk size.
    dcpl = h5py.h5p.create(h5py.h5p.DATASET_CREATE)
    dcpl.set_chunk(chunk)

    # Create the chunked dataset.
    dset = h5py.h5d.create(file, DATASET, h5py.h5t.STD_I32LE, space, dcpl)

    # Define and select the first part of the hyperslab selection.
    start = (0, 0)
    stride = (3, 3)
    count = (2, 3)
    block = (2, 2)
    space.select_hyperslab(start, count, stride, block, h5py.h5s.SELECT_SET)

    # Define and select the second part of the hyperslab selection which is
    # subtracted from the first selection by the use of SELECT_NOTB
    block = (1, 1)
    space.select_hyperslab(start, count, stride, block, h5py.h5s.SELECT_NOTB)

    # Write the data to the dataset.
    dset.write(h5py.h5s.ALL, space, wdata)

    # Force the objects to be closed.
    del dcpl
    del dset
    del space
    del file

    # Now we begin the read section of this example.
    # Open the file and dataset using the default properties.
    file = h5py.h5f.open(FILE)
    dset = h5py.h5d.open(file, DATASET)

    # Retrieve the dataset creation property list and print the storage
    # layout.
    dcpl = dset.get_create_plist()
    layout = dcpl.get_layout()
    msg = "Storage layout for %s is:  " % DATASET
    if layout == h5py.h5d.COMPACT:
        msg += "H5D_COMPACT"
    elif layout == h5py.h5d.CONTIGUOUS:
        msg += "H5D_CONTIGUOUS"
    elif layout == h5py.h5d.CHUNKED:
        msg += "H5D_CHUNKED"
    print(msg)

    # Read the data using the default properties.
    rdata = np.zeros(dims, dtype=np.int32)
    dset.read(h5py.h5s.ALL, h5py.h5s.ALL, rdata)
    print("Data as written to disk by hyperslab:")
    print(rdata)

    # Define and select the hyperslab to use for reading.
    space = dset.get_space()
    start = (0, 1)
    stride = (4, 4)
    count = (2, 2)
    block = (2, 3)
    space.select_hyperslab(start, count, stride, block, h5py.h5s.SELECT_SET)

    # Read the data using the previously defined hyperslab.
    dset.read(h5py.h5s.ALL, space, rdata)
    print("Data as read from disk by hyperslab:")
    print(rdata)


if __name__ == "__main__":
    run()
