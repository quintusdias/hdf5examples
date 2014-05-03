"""
This example shows how to read and write variable-length datatypes to an
attribute.  The program first writes two variable-length integer arrays to a
dataset then closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.

Arbitrary vlens are not supported on versions of h5py before 2.3.0.
"""
import re

import numpy as np
import h5py

FILE = "h5ex_t_vlen.h5"
DATASET = "DS1"
ATTRIBUTE = "DS1"

LEN0 = 3
LEN1 = 12

def run():

    # Initialize variable-length data.  wdata[0] is a countdown of length LEN0,
    # wdata[1] is a Fibonacci sequence of length LEN1
    wdata = [[], []]
    for j in range(LEN0):
        wdata[0].append(LEN0 - j)

    wdata[1] = [1, 1]
    for j in range(2, LEN1):
        wdata[1].append(wdata[1][j - 2] + wdata[1][j - 1])

    dtype = h5py.special_dtype(vlen=np.int32)
    attr = np.array([np.array(wdata[0]), np.array(wdata[1])], dtype=dtype)

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, data=0)
        dset.attrs[ATTRIBUTE] = attr

    with h5py.File(FILE) as f:
        rdata = f[DATASET].attrs[ATTRIBUTE]

    print("%s:" % ATTRIBUTE)
    print(rdata)


if __name__ == "__main__":
    run()        
   


