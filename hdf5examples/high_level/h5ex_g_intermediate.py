"""
This example shows how to create intermediate groups (ridiculously simple)

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

FILE = "h5ex_g_intermediate.h5"
GROUP = "/G1/G2/G3"

def run():

    with h5py.File(FILE, 'w') as f:
        grp = f.create_group(GROUP)

        print("\nObjects in the file:")
        f.visititems(printme)

def printme(name, obj):

    # Let's prepend with a leading slash, just so we have the full path.
    msg = "/{0} ({1})"
    if type(obj) == h5py._hl.group.Group:
        args = (name, "Group")
    elif type(obj) == h5py._hl.dataset.Dataset:
        args = (name, "Dataset")
    elif type(obj) == h5py._hl.datatype.Datatype:
        args = (name, "Datatype")
    print(msg.format(*args))

if __name__ == "__main__":
    run()        
