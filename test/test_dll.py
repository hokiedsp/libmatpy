#!/usr/bin/python3
# from ctypes import *
# import os

# matlabdir = 'C:\\Program Files\\MATLAB\\R2019a\\bin\\win64'
# os.environ['PATH'] = os.environ['PATH']+os.pathsep+matlabdir

# libmat = cdll.LoadLibrary("libmat.dll")
# libmx = cdll.LoadLibrary("libmx.dll")

# libmat.matOpen.restype = c_void_p
# libmat.matOpen.argtypes = [POINTER(c_char), POINTER(c_char)]

# filename = 'D:\\Users\\tikuma\\Documents\\Research\\hsvanalysis-py\\test\\mknpnl_05.had'
# opt = 'r'


# FILE = libmat.matOpen(filename.encode('utf-8'), opt.encode('utf-8'))
# if (not FILE):
#     raise Exception("Invalid file name")

# # char **matGetDir(MATFile *mfp, int *num)
# libmat.matGetDir.restype = POINTER(c_char_p)
# libmat.matGetDir.argtypes = [c_void_p, POINTER(c_int)]

# numvars = c_int()
# pvarnames = libmat.matGetDir(FILE, byref(numvars))
# print(numvars.value)
# # varnames = c_char_p * numvars

# for i in range(numvars.value):
#     print(pvarnames[i])

# libmat.matGetVariable.restype = c_void_p
# libmat.matGetVariable.argtypes = [c_void_p, c_char_p]
# VAR = libmat.matGetVariable(FILE,pvarnames[0])

# libmx.mxGetDimensions.restype = POINTER(c_size_t)
# libmx.mxGetDimensions.argtypes = [c_void_p]
# dims = libmx.mxGetDimensions(VAR)
# print(dims[0],dims[1])

# libmx.mxFree(pvarnames)

import os

matlabdir = 'C:\\Program Files\\MATLAB\\R2019a\\bin\\win64'
os.environ['PATH'] = os.environ['PATH']+os.pathsep+matlabdir

filename = 'D:\\Users\\tikuma\\Documents\\Research\\hsvanalysis-py\\test\\mknpnl_05.had'
# filename = 'test\\testdata.mat'

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'D:\\Users\\tikuma\\Documents\\Research\\hsvanalysis-py')

import libmat

file = libmat.matfile(filename)

# info = file.getNextVariableInfo()
# while info:
#   print(info)
#   info = file.getNextVariableInfo()

for varname in file.getDir():
  var = file.getVariableInfo(varname)
  sz = var.size()
  dims = var.shape()
  print(varname,': ', var.type(), ' ', sz, ' ', dims)

var = file.getVariable('GlottalAxis')
data = var.data()

# var = file.getVariable('TformData')
# data = var.data()['form'].data()
print(data)