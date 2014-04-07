"""
This example shows how to read and write integer datatypes to an attribute. The
program first writes floats to an attribute with a dataspace of DIM0xDIM1, then
closes the file.  Next, it reopens the file, reads back the data, and outputs
it to the screen.
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
        dset = f.create_dataset(DATASET, data=0)
        dset.attrs[ATTRIBUTE] = wdata

    with h5py.File(FILE) as f:
        rdata = f[DATASET].attrs[ATTRIBUTE]

    print("%s:" % ATTRIBUTE)
    print(rdata)


if __name__ == "__main__":
    run()        
   

