"""
This example shows how to read and write string datatypes to a dataset.  The
program first writes strings to a dataset with a dataspace of DIM0, then
closes the file.  Next, it reopens the file, reads back the data, and outputs
it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_stringatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

DIM0 = 4
SDIM = 8

def run():
    wdata = ['Parting', 'is such', 'sweet', 'sorrow']
    
    # Figure out the length of the longest string, use that to construct the
    # fixed string datatype.
    maxlen = max(map(len, wdata))
    dtype = 'S{0}'.format(maxlen)

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, data=0)
        dset.attrs[ATTRIBUTE] = wdata

    with h5py.File(FILE) as f:
        rdata = f[DATASET].attrs[ATTRIBUTE]

    print("%s:" % ATTRIBUTE)
    print(rdata)


if __name__ == "__main__":
    run()        
   

