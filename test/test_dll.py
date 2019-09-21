#!/usr/bin/python3

import sys
import os
filename = 'testdata.mat'
# filename = 'test\\testdata.mat'

matlabdir = 'C:\\Program Files\\MATLAB\\R2019a\\bin\\win64'
os.environ['PATH'] = matlabdir+os.pathsep+os.environ['PATH']

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, os.path.normpath(sys.path[0]+os.sep+'..'))
import libmat

file = libmat.matfile(filename)

print(len(file))

# info = file.getNextVariableInfo()
# while info:
#   print(info)
#   info = file.getNextVariableInfo()

for varname in file.getDir():
    var = file[varname]
    sz = var.size()
    dims = var.shape()
    print(varname, ': ', var.mtype(), ' ', sz, ' ', dims)

