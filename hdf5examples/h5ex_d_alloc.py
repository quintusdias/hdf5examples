"""
This example shows how to set the space allocation time
for a dataset.  The program first creates two datasets,
one with the default allocation time (late) and one with
early allocation time, and displays whether each has been
allocated and their allocation size.  Next, it writes data
to the datasets, and again displays whether each has been
allocated and their allocation size.

Tested with:
    HDF5:   1.8.9/1.8.10
    Python: 2.7.3/3.2.3
    Numpy:  1.7.1/1.7.1
    H5PY:   2.1.0/2.1.2
"""
import sys

import numpy as np
import h5py

FILE = "h5ex_d_alloc.h5"
DATASET1 = "DS1"
DATASET2 = "DS2"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET1 = DATASET1.encode()
    DATASET2 = DATASET2.encode()

DIM0 = 4
DIM1 = 7
FILLVAL = 99

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
    space_id = h5py.h5s.create_simple(dims)

    # Create the dataset creation property list.
    dcpl = h5py.h5p.create(h5py.h5p.DATASET_CREATE)

    # Set the allocation time to "early".
    dcpl.set_alloc_time(h5py.h5d.ALLOC_TIME_EARLY)

    print("%s has late allocation time" % DATASET1);
    print("%s has early allocation time" % DATASET2);

    # Create the datasets using the dataset creation property list.
    dset1 = h5py.h5d.create(fid, DATASET1,
                            h5py.h5t.STD_I32BE, 
                            space_id, h5py.h5p.DEFAULT, h5py.h5p.DEFAULT)
    dset2 = h5py.h5d.create(fid, DATASET2,
                            h5py.h5t.STD_I32BE, 
                            space_id, dcpl, h5py.h5p.DEFAULT)

    # Retrieve and print space status and storage size for dset1.
    space_status = dset1.get_space_status()
    storage_size = dset1.get_storage_size()
    args = (DATASET1, " " if space_status == h5py.h5d.SPACE_STATUS_ALLOCATED else " not ")
    print("Space for %s has%sbeen allocated." % args)
    print("Storage size for %s is:  %d bytes" % (DATASET1, storage_size))

    # Retrieve and print space status and storage size for dset2.
    space_status = dset2.get_space_status()
    storage_size = dset2.get_storage_size()
    args = (DATASET2, " " if space_status == h5py.h5d.SPACE_STATUS_ALLOCATED else " not ")
    print("Space for %s has%sbeen allocated." % args)
    print("Storage size for %s is:  %d bytes" % (DATASET2, storage_size))

    print("Writing data...\n")
    dset1.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)
    dset2.write(h5py.h5s.ALL, h5py.h5s.ALL, wdata)

    # Retrieve and print space status and storage size for dset1.
    space_status = dset1.get_space_status()
    storage_size = dset1.get_storage_size()
    args = (DATASET1, " " if space_status == h5py.h5d.SPACE_STATUS_ALLOCATED else " not ")
    print("Space for %s has%sbeen allocated." % args)
    print("Storage size for %s is:  %d bytes" % (DATASET1, storage_size))

    # Retrieve and print space status and storage size for dset2.
    space_status = dset2.get_space_status()
    storage_size = dset2.get_storage_size()
    args = (DATASET2, " " if space_status == h5py.h5d.SPACE_STATUS_ALLOCATED else " not ")
    print("Space for %s has%sbeen allocated." % args)
    print("Storage size for %s is:  %d bytes" % (DATASET2, storage_size))


if __name__ == "__main__":
    run()        
   
