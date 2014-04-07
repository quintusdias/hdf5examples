"""
This example shows how to read and write string datatypes to a dataset.  The
program first writes strings to a dataset with a dataspace of DIM0, then
closes the file.  Next, it reopens the file, reads back the data, and outputs
it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_vlstringatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

def run():

    # Must use the special variable-length string dtype.
    dtype = h5py.special_dtype(vlen=str)
    wdata = ['Parting', 'is such', 'sweet', 'sorrow']

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, data=0)
        dset.attrs.create(ATTRIBUTE, wdata, dtype=dtype)

    with h5py.File(FILE) as f:
        rdata = f[DATASET].attrs[ATTRIBUTE]

    print("%s:" % ATTRIBUTE)
    print(rdata)


if __name__ == "__main__":
    run()        
   

