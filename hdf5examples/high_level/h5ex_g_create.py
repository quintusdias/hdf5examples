"""
This example shows how to create, open, and close a group.
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
