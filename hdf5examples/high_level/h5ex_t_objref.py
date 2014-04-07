"""
This example shows how to read and write object references to a dataset.  The
program first creates objects in the file and writes references to those 
objects to a dataset with a dataspace of DIM0, then closes the file.  Next it
reopens the file, dereferences the references, and outputs the names of their
targets to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_objref.h5"
DATASET = "DS1"
DIM0 = 2

ref_type = {h5py._hl.dataset.Dataset: 'Dataset',
            h5py._hl.group.Group:  'Group'}
def run():

    with h5py.File(FILE, 'w') as f:
        dset2 = f.create_dataset("DS2", data=0)
        grp = f.create_group("G1")

        dtype = h5py.special_dtype(ref=h5py.Reference)
        dset = f.create_dataset(DATASET, (DIM0,), dtype=dtype)
        dset[...] = [dset2.ref, grp.ref]

    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset[...]

        for ref in rdata:
            print("{0} {1}".format(ref_type[type(f[ref])], f[ref].name))


if __name__ == "__main__":
    run()        
   

