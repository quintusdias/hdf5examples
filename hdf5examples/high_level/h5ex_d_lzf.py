"""
This example shows how to read and write data to a dataset using
LZF compression.  The program first writes integers to a dataset using LZF,
then closes the file.  Next, it reopens the file, reads back the data,
and outputs the type of compression and the maximum value in the dataset
to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_d_lzf.h5"
DATASET = "DS1"

DIM0 = 32
DIM1 = 64
CHUNK0 = 4
CHUNK1 = 8

def run():

    # Initialize the data.
    wdata = np.zeros((DIM0, DIM1), dtype=np.int32)
    for i in range(DIM0):
        for j in range(DIM1):
            wdata[i][j] = i * j - j


    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0, DIM1), chunks=(CHUNK0, CHUNK1),
                                compression='lzf', dtype='<i4')
        dset[...] = wdata


    with h5py.File(FILE) as f:
        dset = f[DATASET]
        print("Filter type for {0} is {1}".format(DATASET, dset.compression))

        rdata = np.zeros((DIM0, DIM1))
        dset.read_direct(rdata)

        # Verify that the dataset was read correctly.
        np.testing.assert_array_equal(rdata, wdata)
        print("Maximum value in DS1 is:  %d" % rdata.max())

if __name__ == "__main__":
    run()
