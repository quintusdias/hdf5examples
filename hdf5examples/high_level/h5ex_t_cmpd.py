"""
This example shows how to read and write compound datatypes to a dataset.  The
program first writes compound structures to a dataset with a dataspace of DIM0,
then closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_cmpd.h5"
DATASET = "DS1"

DIM0 = 4

def run():

    # Create the compound datatype.
    dtype = np.dtype([("Serial number", np.int32), 
                      ("Location",      h5py.special_dtype(vlen=str)),
                      ("Temperature",   np.float),
                      ("Pressure",      np.float)])

    wdata = np.zeros((DIM0,), dtype=dtype)
    wdata['Serial number'] = (1153, 1184, 1027, 1313)
    wdata['Location'] = ("Exterior (static)", "Intake", "Intake manifold",
                         "Exhaust manifold")
    wdata['Temperature'] = (53.23, 55.12, 103.55, 1252.89)
    wdata['Pressure'] = (24.57, 22.95, 31.23, 84.11)

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0,), dtype=dtype)
        dset[...] = wdata


    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset[...]

    print("%s:" % DATASET)
    print("\tSerial number:  {0}".format(rdata["Serial number"]))
    print("\tLocation:  {0}".format(rdata["Location"]))
    print("\tTemperature:  {0}".format(rdata["Temperature"]))
    print("\tPressure:  {0}".format(rdata["Pressure"]))


if __name__ == "__main__":
    run()        
   

