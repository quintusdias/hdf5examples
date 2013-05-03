"""
This example shows how to set the fill value for a dataset.  The
program first sets the fill value to FILLVAL, creates a dataset
with dimensions of DIM0xDIM1, reads from the uninitialized dataset,
and outputs the contents to the screen.  Next, it writes integers
to the dataset, reads the data back, and outputs it to the screen.
Finally it extends the dataset, reads from it, and outputs the
result to the screen.

Tested with:
    HDF5:   1.8.9/1.8.10
    Python: 2.7.3/3.2.3
    Numpy:  1.7.1/1.7.1
    H5PY:   2.1.0/2.1.2
"""
import sys

import numpy as np
import h5py

FILE = "h5ex_d_fillval.h5"
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
FILLVAL = 99

def run():
    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i * j - j

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create the dataspace.  
    dims = (DIM0, DIM1)
    maxdims = (h5py.h5s.UNLIMITED, h5py.h5s.UNLIMITED)
    space_id = h5py.h5s.create_simple(dims, maxdims)

    # Create the dataset creation property list.  Set the layout to compact.
    dcpl = h5py.h5p.create(h5py.h5p.DATASET_CREATE)
    chunk = (CHUNK0, CHUNK1)
    dcpl.set_chunk(chunk)

    # Set the fill value for the dataset.
    dcpl.set_fill_value(np.array(FILLVAL))

    # Set the allocation time to "early".  This way we can be sure that
    # reading from the dataset immediately after creation will return the
    # fill value
    dcpl.set_alloc_time(h5py.h5d.ALLOC_TIME_EARLY)

    # Create the datasets using the dataset creation property list.
    dset = h5py.h5d.create(fid, DATASET, h5py.h5t.STD_I32LE, space_id, dcpl)

    # Read from the dataset, which has not been written to yet.
    print("\nDataset before being written to:")
    rdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    dset.read(h5py.h5s.ALL,h5py.h5s.ALL, rdata)
    print(rdata)

    # Write the data to the dataset.
    dset.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)

    # Read the data back.
    print("\nDataset after being written to:")
    rdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    dset.read(h5py.h5s.ALL,h5py.h5s.ALL, rdata)
    print(rdata)

    # Extend the dataset.
    extdims = (EDIM0, EDIM1)
    dset.set_extent(extdims)

    # Read from the extended dataset.
    print("\nDataset after extension:")
    rdata2 = np.zeros((EDIM0, EDIM1), dtype=np.int32)
    dset.read(h5py.h5s.ALL,h5py.h5s.ALL, rdata2)
    print(rdata2)

if __name__ == "__main__":
    run()        
