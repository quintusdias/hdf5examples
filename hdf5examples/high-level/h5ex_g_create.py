"""
This example shows how to create, open, and close a group.

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

FILE = "h5ex_g_create.h5"
GROUP = "/G1"

def run():

    with h5py.File(FILE, 'w') as f:
        grp = f.create_group(GROUP)

    # Re-open the group, obtaining a new handle.
    with h5py.File(FILE) as f:
        grp = f[GROUP]

if __name__ == "__main__":
    run()        
