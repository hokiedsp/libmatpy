# libmatpy: C++ wrapper for libmat, MATLAB C API to Read MAT-File Data

**NOTE:** This wrapper requires locally installed Matlab (Release 2018a or later) to access the required shared libraries

**TODO:**
- [ ] Complete the test script
- [ ] Test on OSX and Linux
- [ ] Add support for writing

## Setup

1. Download libmat.py into the appropriate place in your project folder
2. Add path to the Matlab folder containing libmat and libmx libraries to `os.environ['PATH']`

    For Matlab R2019a on Windows, 

    ```python
    import os
    matlabdir = 'C:\\Program Files\\MATLAB\\R2019a\\bin\\win64'
    os.environ['PATH'] = matlabdir+os.pathsep+os.environ['PATH']
    ```

    Here, it's important to prepend the Matlab path to avoid `libmat.dll` to load incorrect dependent DLLs.

### Alternate way

This Python module could also be by using this repository as a whole as a git submodule of your project. In that case, the submodule directory becomes Python package, and you can access the 2 classes in the module as `libmatpy.matfile` and `libmatpy.matlab_array` assuming the submodule directory is named `libmatpy`

## Basic Use

0. Import the module (assuming the module is placed in one of the `sys.path` paths):

    ```python
    import libmat
    ```

    then create `libmat.matfile` class object

1. Open the MAT files

    ```python
    matfilename = 'mydata.mat' # assume contains variables x, y, and z
    FILE = libmat.matfile(matfilename)
    ```

2. Get the variable list

    ```python
    varnames = FILE.getDir()
    print(varnames) # prints ['x', 'y', 'z']
    ```

3. `libmat.matfile` is a custom sequential class, so its variables can be accessed via `self[key]` notation. Its items are `libmat.matlab_array` objects and their basic attributes are obtained via `mtype()`, `size()`, `shape()`, and `data()` methods:

    ```python
        var = file['x']     # libmat.matlab_array object for the stored variable x
        sz = var.size()     # number of elements (integer)
        dims = var.shape()  # array dimensions (tuple of numbers)
        mtype = var.mtype() # matlab data type (string)
        data = var.data()   # data content (depends on mtype)
    ```

    **NOTE**: For non-scalar data, `data()` returns a `numpy.ndarary` object. It uses the raw data pointer returned from the dynamic library. So, make sure that the originating `libmat.matlab_array` object remain in the memory while `data` is being use.
  