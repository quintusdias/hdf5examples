"""
This example shows how to create and extend an unlimited dataset.
The program first writes integers to a dataset with dataspace
dimensions of DIM0xDIM1, then closes the file.  Next, it reopens
the file, reads back the data, outputs it to the screen, extends
the dataset, and writes new data to the extended portions of the
dataset.  Finally it reopens the file again, reads back the data,
and outputs it to the screen.

Tested with:
    Fedora 18:
        HDF5 1.8.9, Python 2.7.3, Numpy 1.7.1, h5py 2.1.3
    Fedora 18:
        HDF5 1.8.9, Python 3.3.0, Numpy 1.7.1, h5py 2.1.3
    Mac OS X 10.6.8:
        HDF5 1.8.10, Python 3.2.5, Numpy 1.7.1, h5py 2.1.3
"""
import numpy as np
import h5py

FILE = "h5ex_d_unlimadd.h5"
DATASET = "DS1"

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

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0, DIM1), maxshape=(None, None),
                                chunks=(CHUNK0, CHUNK1), compression='gzip',
                                dtype='<i4')
        dset[...] = wdata

    with h5py.File(FILE, 'r+') as f:
        dset = f[DATASET]
        rdata = dset[...]

        print("\nDataset before extension:")
        print(rdata)

        # Extend the dataset.
        dset.resize((EDIM0, EDIM1))

        # Initialize data for writing to the extended dataset.
        wdata = np.zeros((EDIM0, EDIM1), dtype=np.int32)
        for i in range(EDIM0):
            for j in range(EDIM1):
                wdata[i][j] = j

        # The corresponding C API example writes the data using a hyperslab
        # subtraction.  This does not translate well into the high level
        # h5py API (it *IS* available in the low-level h5py API, however).
        # The same effect can be achieved with two writes instead of one.
        dset[DIM0:EDIM0, 0:EDIM1] = wdata[DIM0:EDIM0, 0:EDIM1]
        dset[0:DIM0, DIM1:EDIM1] = wdata[0:DIM0, DIM1:EDIM1]

    # Now simply read back the data and echo to the screen.
    with h5py.File(FILE, 'r') as f:
        dset = f[DATASET]
        rdata = dset[...]
        print("\nDataset after extension:")
        print(rdata)

if __name__ == "__main__":
    run()
