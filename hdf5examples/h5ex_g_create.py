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
import sys

import numpy as np
import h5py

FILE = "h5ex_g_create.h5"
GROUP = "/G1"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    GROUP = GROUP.encode()

def run():

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create a group named "G1" in the file.
    group = h5py.h5g.create(fid, GROUP)

    # Close the group.  The handle "group" can no longer be used.
    del group

    # Re-open the group, obtaining a new handle.
    group = h5py.h5g.open(fid, GROUP)

    # Close and release resources.
    del group
    del fid


if __name__ == "__main__":
    run()        
