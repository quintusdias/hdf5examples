"""
This example shows how to read and write integer datatypes to an attribute. The
program first writes floats to an attribute with a dataspace of DIM0xDIM1, then
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
import numpy as np
import h5py

FILE = "h5ex_t_intatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

DIM0 = 4
DIM1 = 7
DIMS = (DIM0, DIM1)

def run():
    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int64)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i * j - j

    with h5py.File(FILE, 'w') as f:
        # Create a dataset with a scalar dataspace.
        # The origin C example uses a NULL dataspace, but this does not seem to
        # yet be possible in H5PY?
        dset = f.create_dataset(DATASET, data=0)

        dset.attrs[ATTRIBUTE] = wdata

    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset.attrs[ATTRIBUTE]

    # Output the data to the screen.
    print("%s:" % ATTRIBUTE)
    print(rdata)


if __name__ == "__main__":
    run()        
   

