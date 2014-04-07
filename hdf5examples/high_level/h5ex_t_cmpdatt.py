"""
This example shows how to read and write compound datatypes to an attribute.
The program first writes compound structures to an attribute with a dataspace
of DIM0, then closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_cmpdatt.h5"
DATASET = "DS1"
ATTRIBUTE = "A1"

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
        dset = f.create_dataset(DATASET, data=0)
        dset.attrs.create(ATTRIBUTE, wdata, dtype=dtype)

    with h5py.File(FILE) as f:
        rdata = f[DATASET].attrs[ATTRIBUTE]

    print("%s:" % ATTRIBUTE)
    print("\tSerial number:  {0}".format(rdata["Serial number"]))
    print("\tLocation:  {0}".format(rdata["Location"]))
    print("\tTemperature:  {0}".format(rdata["Temperature"]))
    print("\tPressure:  {0}".format(rdata["Pressure"]))


if __name__ == "__main__":
    run()        
   

