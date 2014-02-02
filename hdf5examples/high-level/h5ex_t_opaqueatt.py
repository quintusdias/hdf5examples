"""
This example shows how to read and write opaque datatypes to a dataset.
The program first writes opaque values to a dataset with a dataspace of DIM0,
then closes the file.  Next, it reopens the file, reads back the data,
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

FILE = "h5ex_t_opaqueatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

DIM0 = 4
LEN = 7

def run():

    # Initialize the data. Use the Numpy void datatype to stand in for
    # H5T_OPAQUE
    dtype=np.dtype('V7')
    wdata = np.zeros((DIM0,), dtype=dtype)
    for i in range(DIM0):
        wdata[i]= b'OPAQUE' + bytes([i + 48])

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, data=0)
        dset.attrs.create(ATTRIBUTE, wdata, dtype=dtype)

    with h5py.File(FILE) as f:
        rdata = f[DATASET].attrs[ATTRIBUTE]

    print("%s:" % DATASET)
    for row in rdata:
        print(row.tostring())

if __name__ == "__main__":
    run()        
   

