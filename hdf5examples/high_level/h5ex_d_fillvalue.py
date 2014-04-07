"""
This example shows how to set the fill value for a dataset.  The
program first sets the fill value to FILLVAL, creates a dataset
with dimensions of DIM0xDIM1, reads from the uninitialized dataset,
and outputs the contents to the screen.  Next, it writes integers
to the dataset, reads the data back, and outputs it to the screen.
Finally it extends the dataset, reads from it, and outputs the
result to the screen.
"""

import numpy as np
import h5py

FILE = "h5ex_d_fillval.h5"
DATASET = "DS1"

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

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0, DIM1), maxshape=(None, None),
                                chunks=(CHUNK0, CHUNK1), fillvalue=FILLVAL,
                                dtype='<i4')

        # Read from the dataset, which has not been written to yet.
        print("\nDataset before being written to:")
        rdata = np.zeros((DIM0, DIM1), dtype=np.int32)
        dset.read_direct(rdata)
        print(rdata)

        # Write the data to the dataset.
        dset[...] = wdata

        # Read the data back.
        print("\nDataset after being written to:")
        rdata = np.zeros((DIM0, DIM1), dtype=np.int32)
        dset.read_direct(rdata)
        print(rdata)

        # Extend the dataset.
        dset.resize((EDIM0, EDIM1))

        # Read from the extended dataset.
        print("\nDataset after extension:")
        rdata2 = np.zeros((EDIM0, EDIM1), dtype=np.int32)
        dset.read_direct(rdata2)
        print(rdata2)

if __name__ == "__main__":
    run()
