"""
This example shows how to read and write data to a dataset using
the Fletcher32 checksum filter.
"""

import numpy as np
import h5py

FILE = "h5ex_d_checksum.h5"
DATASET = "DS1"

DIM0 = 32
DIM1 = 64
CHUNK0 = 4
CHUNK1 = 8

def run():

    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i * j - j

    # Create the dataset with chunking and the Fletcher32 filter.
    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0, DIM1), chunks=(CHUNK0, CHUNK1),
                                fletcher32=True, dtype='<i4')
        dset[...] = wdata

    with h5py.File(FILE) as f:
        dset = f[DATASET]
        if f[DATASET].fletcher32:
            print("Filter type is H5Z_FILTER_FLETCHER32.")
        else:
            raise RuntimeError("Fletcher32 filter not retrieved.")

        rdata = np.zeros((DIM0, DIM1))
        dset.read_direct(rdata)

    # Verify that the dataset was read correctly.
    np.testing.assert_array_equal(rdata, wdata)


if __name__ == "__main__":
    run()
