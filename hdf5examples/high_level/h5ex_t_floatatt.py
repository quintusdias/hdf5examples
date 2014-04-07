"""
This example shows how to read and write float datatypes to an attribute. The
program first writes floats to an attribute with a dataspace of DIM0xDIM1, then
closes the file.  Next, it reopens the file, reads back the data, and outputs
it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_floatatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

DIM0 = 4
DIM1 = 7
DIMS = (DIM0, DIM1)

def run():
    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.float64)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i / (j + 0.5) + j

    with h5py.File(FILE, 'w') as f:
        # Create a dataset with a scalar dataspace.
        # The origin C example uses a NULL dataspace, but this does not seem to
        # yet be possible in H5PY?
        dset = f.create_dataset(DATASET, data=0)

        dset.attrs[ATTRIBUTE] = wdata


    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset.attrs[ATTRIBUTE]

    print("%s:" % ATTRIBUTE)
    print(rdata)


if __name__ == "__main__":
    run()        
   

