"""
This example shows how to read and write enumerated attributes to a dataset.
The program first writes enumerate values to an attribute with a dataspace of
DIM0xDIM1 then closes the file.  Next, it reopens the file, reads back the data,
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

FILE = "h5ex_t_enumatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

DIM0 = 4
DIM1 = 7

def run():

    # Create the enum datatype.
    mapping = {'SOLID': 0, 'LIQUID': 1, 'GAS': 2, 'PLASMA': 3}
    dtype = h5py.special_dtype(enum=(np.int16, mapping))

    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = ((i + 1) * j - j) % (mapping['PLASMA'] + 1)

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, data=0)
        dset.attrs.create(ATTRIBUTE, wdata, dtype=dtype)

    with h5py.File(FILE) as f:
        rdata = f[DATASET].attrs[ATTRIBUTE]

    # Make the inverse mapping so that it's easier to interpret the output.
    inv_mapping = {v:k for (k,v) in mapping.items()}
    print("%s:" % ATTRIBUTE)
    for row in rdata:
        print([inv_mapping[item] for item in row])


if __name__ == "__main__":
    run()        
   

