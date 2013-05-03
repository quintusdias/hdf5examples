"""
This example shows how to create intermediate groups with a single call to
h5py.h5g.create.

Tested with:
    HDF5:   1.8.9/1.8.10
    Python: 2.7.3/3.2.3
    Numpy:  1.7.1/1.7.1
    H5PY:   2.1.0/2.1.2
"""
import sys

import numpy as np
import h5py

FILE = "h5ex_g_intermediate.h5"
GROUP = "/G1/G2/G3"

# Strings are handled very differently between python2 and python3.
if sys.hexversion >= 0x03000000:
    FILE = FILE.encode()
    GROUP = GROUP.encode()

def run():

    # Create a new file using the default properties.
    fid = h5py.h5f.create(FILE)

    # Create group creation property list and set it to allow creation of
    # intermediate groups.
    gcpl = h5py.h5p.create(h5py.h5p.LINK_CREATE)
    gcpl.set_create_intermediate_group(True)

    # Create a group named "G1" in the file.
    group = h5py.h5g.create(fid, GROUP, gcpl)

    # Print all the objects in the file to show that intermediate groups
    # have been created.
    print("\nObjects in the file:")
    h5py.h5o.visit(fid, op_func, info=True)

    # Close the group.  The handle "group" can no longer be used.
    del gcpl
    del group
    del fid

def op_func(name, info):

    # Let's prepend with a leading slash, just so we have the full path.
    if info.type == h5py.h5o.TYPE_GROUP:
        fmt = "/%s (Group)"
    elif info.type == h5py.h5o.TYPE_DATASET:
        fmt = "/%s (Dataset)"
    elif info.type == h5py.h5o.TYPE_NAMED_DATATYPE:
        fmt = "/%s (Datatype)"
    else:
        fmt = "/%s (Unknown)"
    print( fmt % name.decode('utf-8'))

if __name__ == "__main__":
    run()        
