"""
This example illustrates how to create a compressed dataset.

Tested with:
    Fedora 18:
        HDF5 1.8.9, Python 2.7.3, Numpy 1.7.1, h5py 2.1.3
    Fedora 18:
        HDF5 1.8.9, Python 3.3.0, Numpy 1.7.1, h5py 2.1.3
    Mac OS X 10.6.8:
        HDF5 1.8.10, Python 3.2.5, Numpy 1.7.1, h5py 2.1.3
"""
import sys

import numpy as np
import h5py

FILE = "cmprss.h5"
DATASET = "Compressed_Data"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    DATASET = DATASET.encode()

DIM0 = 100
DIM1 = 20

def run():
    # Create a file.
    fid = h5py.h5f.create(FILE)

    # Create dataset "Compressed Data" in the group using absolute names.
    dims = (DIM0, DIM1)
    space_id = h5py.h5s.create_simple(dims)

    dcpl = h5py.h5p.create(h5py.h5p.DATASET_CREATE)

    # Datasets must be chunked for compression.
    cdims = (20, 20)
    dcpl.set_chunk(cdims)

    # Set ZLIB / DEFLATE compression using compression level 6.
    dcpl.set_deflate(6)

    dset = h5py.h5d.create(fid, DATASET,
                           h5py.h5t.STD_I32BE, 
                           space_id, dcpl, h5py.h5p.DEFAULT)

    buf = np.zeros((DIM0, DIM1))
    for i in range(DIM0):
        buf[i] = i + np.arange(DIM1)

    dset.write(h5py.h5s.ALL, h5py.h5s.ALL, buf)

    # Now reopen the file and dataset.
    fid = h5py.h5f.open(FILE)
    dset = h5py.h5d.open(fid, DATASET)

    dcpl = dset.get_create_plist()

    numfilt = dcpl.get_nfilters()
    print("Number of filters associated with dataset:  %d" % numfilt)

    for j in range(numfilt):
        code, flags, values, name = dcpl.get_filter(j)
        print(name)

    newdata = np.zeros((DIM0, DIM1))
    dset.read(h5py.h5s.ALL,h5py.h5s.ALL, newdata)
    print(newdata)

if __name__ == "__main__":
    run()

