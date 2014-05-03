"""
This example shows how to read and write variable-length datatypes to a
dataset.  The program first writes two variable-length integer arrays to a
dataset then closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.

Arbitrary vlens are not supported on versions of h5py before 2.3.0.
"""
import re

import numpy as np
import h5py

FILE = "h5ex_t_vlen.h5"
DATASET = "DS1"

LEN0 = 3
LEN1 = 12

def run():

    # Initialize variable-length data.  wdata[0] is a countdown of length LEN0,
    # wdata[1] is a Fibonacci sequence of length LEN1
    wdata0 = np.arange(LEN0, 0, -1)
    wdata1 = np.zeros((LEN1,))
    wdata1[0] = 1
    wdata1[1] = 1
    for j in range(2, LEN1):
        wdata1[j] = wdata1[j - 2] + wdata1[j - 1]

    wdata = [wdata0, wdata1]

    dtype = h5py.special_dtype(vlen=np.dtype('int32'))
    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (2,), dtype=dtype)
        dset[...] = wdata

    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset[...]

    print("%s:" % DATASET)
    print(rdata)


if __name__ == "__main__":
    run()        
   

