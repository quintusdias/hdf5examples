"""
This example shows how to read and write string datatypes to a dataset.  The
program first writes strings to a dataset with a dataspace of DIM0, then
closes the file.  Next, it reopens the file, reads back the data, and outputs
it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_string.h5"
DATASET = "DS1"

DIM0 = 4
SDIM = 8

def run():
    wdata = ['Parting', 'is such', 'sweet', 'sorrow']
    
    # Figure out the length of the longest string, use that to construct the
    # datatype.
    maxlen = max(map(len, wdata))
    dtype = 'S{0}'.format(maxlen)

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0,), dtype=dtype)
        dset[...] = wdata

    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset[...]

    # Output the data to the screen.
    print("%s:" % DATASET)
    print(rdata)


if __name__ == "__main__":
    run()        
   

