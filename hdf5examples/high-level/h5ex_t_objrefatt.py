"""
This example shows how to read and write object references to a dataset.  The
program first creates objects in the file and writes references to those 
objects to a dataset with a dataspace of DIM0, then closes the file.  Next it
reopens the file, dereferences the references, and outputs the names of their
targets to the screen.

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

FILE = "h5ex_t_objref.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"
DIM0 = 2

ref_type = {h5py._hl.dataset.Dataset: 'Dataset',
            h5py._hl.group.Group:  'Group'}
def run():

    with h5py.File(FILE, 'w') as f:
        # Create a scalar dataset and group to serve as targets of the 
        # reference attribute.
        dset2 = f.create_dataset("DS2", data=0)
        grp = f.create_group("G1")
        wdata = [dset2.ref, grp.ref]

        # Create a scalar dataset to hold the attribute of references.
        dset = f.create_dataset(DATASET, data=0)
        dtype = h5py.special_dtype(ref=h5py.Reference)
        dset.attrs.create(ATTRIBUTE, wdata, dtype=dtype)

    with h5py.File(FILE) as f:
        rdata = f[DATASET].attrs[ATTRIBUTE]

        for ref in rdata:
            print("{0} {1}".format(ref_type[type(f[ref])], f[ref].name))


if __name__ == "__main__":
    run()        
   

