import glob
import os
import sys
if sys.hexversion < 0x03000000:
    from StringIO import StringIO
else:
    from io import StringIO

import unittest

import numpy as np
import pkg_resources

import hdf5examples

class TestHdf5Examples(unittest.TestCase):

    def setUp(self):
        # Save sys.stdout.
        self.stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore stdout.
        sys.stdout = self.stdout

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # Delete all the hdf5 files.
        lst = glob.glob('h5ex_?_*.h5')
        for h5file in lst:
            os.unlink(h5file)
        others = ['copy1.h5', 'copy2.h5', 'cmprss.h5']
        for other in others:
            if os.path.exists(other):
                os.unlink(other)


    def test_all(self):
        # Just run all the examples.
        for x in dir(hdf5examples.low_level):
            example = getattr(hdf5examples.low_level, x)
            if hasattr(example, 'run'):
                
                # Szip not available on my machine.
                if x == 'h5ex_d_szip':
                    with self.assertRaises(RuntimeError):
                        example.run()
                elif x == 'h5ex_g_visit':
                    hdf5file = pkg_resources.resource_filename(hdf5examples.__name__,
                                                               "data/h5ex_g_visit.h5")
                    example.run(hdf5file)

                elif ((x == 'h5ex_t_vlen' or x == 'h5ex_t_vlenatt') and
                        re.match(r'''1|2\.[012]''', h5py.__version__)):
                    # arbitrary vlens not supported until 2.3.0
                    pass
                else:
                    example.run()


        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()

