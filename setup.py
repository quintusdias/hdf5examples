from distutils.core import setup
setup(name='hdf5examples',
      version='0.0.1',
      description='Example HDF5 codes from THG rewritten in Python',
      long_description=open('README.md').read(),
      author='John Evans',
      author_email='john.g.evans.ne@gmail.com',
      url='https://github.com/quintusdias/hdf5examples',
      packages=['hdf5examples', 'hdf5examples.tests'],
      package_data={'hdf5examples': ['data/*.h5']},
      license='MIT',
      platforms=['darwin'],
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: Implementation :: CPython",
          "License :: OSI Approved :: MIT License",
          "Development Status :: 1 - Alpha",
          "Operating System :: MacOS",
          "Operating System :: POSIX :: Linux",
          "Intended Audience :: Scientific/Research",
          "Intended Audience :: Information Technology",
          "Topic :: Software Development :: Libraries :: Python Modules"
          ]
      )
