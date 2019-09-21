# Wrapper class for _libmat MATLAB C API to Read MAT-File Data

from ctypes import *
import numpy as np
import platform
import os
import sys


class MATFile(Structure):  # C API opaque objects
    pass


MATFile_p = POINTER(MATFile)


class mxArray(Structure):
    pass


mxArray_p = POINTER(mxArray)

libexts = {'Linux': '.so',
           'Darwin': '.dylib',
           'Windows': '.dll'}
libext = libexts[platform.system()]

# C API loading & registering arguments
_libmat = cdll.LoadLibrary('libmat'+libext)
_libmat.matOpen_800.restype = MATFile_p
_libmat.matOpen_800.argtypes = [POINTER(c_char), POINTER(c_char)]
_libmat.matClose_800.restype = c_int
_libmat.matClose_800.argtypes = [MATFile_p]
_libmat.matGetVariable_800.restype = mxArray_p
_libmat.matGetVariable_800.argtypes = [MATFile_p, POINTER(c_char)]
_libmat.matGetVariableInfo_800.restype = mxArray_p
_libmat.matGetVariableInfo_800.argtypes = [MATFile_p, POINTER(c_char)]
_libmat.matGetNextVariable_800.restype = mxArray_p
_libmat.matGetNextVariable_800.argtypes = [MATFile_p, POINTER(POINTER(c_char))]
_libmat.matGetNextVariableInfo_800.restype = mxArray_p
_libmat.matGetNextVariableInfo_800.argtypes = [
    MATFile_p, POINTER(POINTER(c_char))]
_libmat.matPutVariable_800.restype = c_int
_libmat.matPutVariable_800.argtypes = [MATFile_p, POINTER(c_char), mxArray_p]
_libmat.matPutVariableAsGlobal_800.restype = c_int
_libmat.matPutVariableAsGlobal_800.argtypes = [
    MATFile_p, POINTER(c_char), mxArray_p]
_libmat.matDeleteVariable_800.restype = c_int
_libmat.matDeleteVariable_800.argtypes = [MATFile_p, POINTER(c_char)]
_libmat.matGetDir_800.restype = POINTER(c_char_p)
_libmat.matGetDir_800.argtypes = [MATFile_p, POINTER(c_int)]
_libmat.matGetFp_800.restype = c_void_p
_libmat.matGetFp_800.argtypes = [MATFile_p]
_libmat.matGetErrno_800.restype = c_int
_libmat.matGetErrno_800.argtypes = [MATFile_p]

# C API for matrix operations
_libmx = cdll.LoadLibrary('libmx'+libext)
_libmx.mxMalloc_800.restype = c_void_p
_libmx.mxMalloc_800.argtypes = [c_size_t]
_libmx.mxCalloc_800.restype = c_void_p
_libmx.mxCalloc_800.argtypes = [c_size_t, c_size_t]
_libmx.mxFree_800.argtypes = [c_void_p]
_libmx.mxRealloc_800.restype = c_void_p
_libmx.mxRealloc_800.argtypes = [c_void_p, c_size_t]
_libmx.mxGetNumberOfDimensions_800.restype = c_size_t
_libmx.mxGetNumberOfDimensions_800.argtypes = [mxArray_p]
_libmx.mxGetDimensions_800.restype = POINTER(c_size_t)
_libmx.mxGetDimensions_800.argtypes = [mxArray_p]
_libmx.mxGetM_800.restype = c_size_t
_libmx.mxGetM_800.argtypes = [mxArray_p]
_libmx.mxGetIr_800.restype = POINTER(c_size_t)
_libmx.mxGetIr_800.argtypes = [mxArray_p]
_libmx.mxGetJc_800.restype = POINTER(c_size_t)
_libmx.mxGetJc_800.argtypes = [mxArray_p]
_libmx.mxGetNzmax_800.restype = c_size_t
_libmx.mxGetNzmax_800.argtypes = [mxArray_p]
_libmx.mxSetNzmax_800.argtypes = [mxArray_p, c_size_t]
_libmx.mxGetFieldNameByNumber_800.restype = c_char_p
_libmx.mxGetFieldNameByNumber_800.argtypes = [mxArray_p, c_int]
_libmx.mxGetFieldByNumber_800.restype = mxArray_p
_libmx.mxGetFieldByNumber_800.argtypes = [mxArray_p, c_size_t, c_int]
_libmx.mxGetCell_800.restype = mxArray_p
_libmx.mxGetCell_800.argtypes = [mxArray_p, c_size_t]
_libmx.mxGetClassID_800.restype = c_int
_libmx.mxGetClassID_800.argtypes = [mxArray_p]
_libmx.mxGetData_800.restype = c_void_p
_libmx.mxGetData_800.argtypes = [mxArray_p]
_libmx.mxSetData_800.argtypes = [mxArray_p, c_void_p]
_libmx.mxIsNumeric_800.restype = c_bool
_libmx.mxIsNumeric_800.argtypes = [mxArray_p]
_libmx.mxIsCell_800.restype = c_bool
_libmx.mxIsCell_800.argtypes = [mxArray_p]
_libmx.mxIsLogical_800.restype = c_bool
_libmx.mxIsLogical_800.argtypes = [mxArray_p]
_libmx.mxIsScalar_800.restype = c_bool
_libmx.mxIsScalar_800.argtypes = [mxArray_p]
_libmx.mxIsChar_800.restype = c_bool
_libmx.mxIsChar_800.argtypes = [mxArray_p]
_libmx.mxIsStruct_800.restype = c_bool
_libmx.mxIsStruct_800.argtypes = [mxArray_p]
_libmx.mxIsOpaque_800.restype = c_bool
_libmx.mxIsOpaque_800.argtypes = [mxArray_p]
_libmx.mxIsFunctionHandle_800.restype = c_bool
_libmx.mxIsFunctionHandle_800.argtypes = [mxArray_p]
# c_void_p mxGetImagData(mxArray_p)
# void mxSetImagData(mxArray_p, c_void_p)
_libmx.mxIsComplex_800.restype = c_bool
_libmx.mxIsComplex_800.argtypes = [mxArray_p]
_libmx.mxIsSparse_800.restype = c_bool
_libmx.mxIsSparse_800.argtypes = [mxArray_p]
_libmx.mxIsDouble_800.restype = c_bool
_libmx.mxIsDouble_800.argtypes = [mxArray_p]
_libmx.mxIsSingle_800.restype = c_bool
_libmx.mxIsSingle_800.argtypes = [mxArray_p]
_libmx.mxIsInt8_800.restype = c_bool
_libmx.mxIsInt8_800.argtypes = [mxArray_p]
_libmx.mxIsUint8_800.restype = c_bool
_libmx.mxIsUint8_800.argtypes = [mxArray_p]
_libmx.mxIsInt16_800.restype = c_bool
_libmx.mxIsInt16_800.argtypes = [mxArray_p]
_libmx.mxIsUint16_800.restype = c_bool
_libmx.mxIsUint16_800.argtypes = [mxArray_p]
_libmx.mxIsInt32_800.restype = c_bool
_libmx.mxIsInt32_800.argtypes = [mxArray_p]
_libmx.mxIsUint32_800.restype = c_bool
_libmx.mxIsUint32_800.argtypes = [mxArray_p]
_libmx.mxIsInt64_800.restype = c_bool
_libmx.mxIsInt64_800.argtypes = [mxArray_p]
_libmx.mxIsUint64_800.restype = c_bool
_libmx.mxIsUint64_800.argtypes = [mxArray_p]
_libmx.mxGetNumberOfElements_800.restype = c_size_t
_libmx.mxGetNumberOfElements_800.argtypes = [mxArray_p]
# POINTER(c_double) mxGetPi(mxArray_p);
# void mxSetPi(mxArray_p, POINTER(c_double) );
_libmx.mxGetChars_800.restype = POINTER(c_wchar)
_libmx.mxGetChars_800.argtypes = [mxArray_p]
_libmx.mxGetUserBits_800.restype = c_int
_libmx.mxGetUserBits_800.argtypes = [mxArray_p]
_libmx.mxSetUserBits_800.argtypes = [mxArray_p, c_int]
_libmx.mxGetScalar_800.restype = c_double
_libmx.mxGetScalar_800.argtypes = [mxArray_p]
_libmx.mxIsFromGlobalWS_800.restype = c_bool
_libmx.mxIsFromGlobalWS_800.argtypes = [mxArray_p]
_libmx.mxSetFromGlobalWS_800.argtypes = [mxArray_p, c_bool]
_libmx.mxSetM_800.argtypes = [mxArray_p, c_size_t]
_libmx.mxGetN_800.restype = c_size_t
_libmx.mxGetN_800.argtypes = [mxArray_p]
_libmx.mxIsEmpty_800.restype = c_bool
_libmx.mxIsEmpty_800.argtypes = [mxArray_p]
_libmx.mxGetFieldNumber_800.restype = c_int
_libmx.mxGetFieldNumber_800.argtypes = [mxArray_p, c_char_p]
_libmx.mxSetIr_800.argtypes = [mxArray_p, POINTER(c_size_t)]
_libmx.mxSetJc_800.argtypes = [mxArray_p, POINTER(c_size_t)]
_libmx.mxGetData_800.restype = c_void_p
_libmx.mxGetData_800.argtypes = [mxArray_p]
_libmx.mxSetData_800.argtypes = [mxArray_p, c_void_p]
_libmx.mxGetPr_800.restype = POINTER(c_double)
_libmx.mxGetPr_800.argtypes = [mxArray_p]
_libmx.mxSetPr_800.argtypes = [mxArray_p, POINTER(c_double)]
_libmx.mxGetElementSize_800.restype = c_size_t
_libmx.mxGetElementSize_800.argtypes = [mxArray_p]
_libmx.mxCalcSingleSubscript_800.restype = c_size_t
_libmx.mxCalcSingleSubscript_800.argtypes = [
    mxArray_p, c_size_t, POINTER(c_size_t)]
_libmx.mxGetNumberOfFields_800.restype = c_int
_libmx.mxGetNumberOfFields_800.argtypes = [mxArray_p]
_libmx.mxSetCell_800.argtypes = [mxArray_p, c_size_t, mxArray_p]
_libmx.mxSetFieldByNumber_800.argtypes = [
    mxArray_p, c_size_t, c_int, mxArray_p]
_libmx.mxGetField_800.restype = mxArray_p
_libmx.mxGetField_800.argtypes = [mxArray_p, c_size_t, c_char_p]
_libmx.mxSetField_800.argtypes = [mxArray_p, c_size_t, c_char_p, mxArray_p]
_libmx.mxGetProperty_800.restype = mxArray_p
_libmx.mxGetProperty_800.argtypes = [mxArray_p, c_size_t, c_char_p]
_libmx.mxSetProperty_800.argtypes = [mxArray_p, c_size_t, c_char_p, mxArray_p]
_libmx.mxGetClassName_800.restype = c_char_p
_libmx.mxGetClassName_800.argtypes = [mxArray_p]
_libmx.mxIsClass_800.restype = c_bool
_libmx.mxIsClass_800.argtypes = [mxArray_p, c_char_p]
_libmx.mxCreateNumericMatrix_800.restype = mxArray_p
_libmx.mxCreateNumericMatrix_800.argtypes = [c_size_t, c_size_t, c_int, c_int]
_libmx.mxCreateUninitNumericMatrix_800.restype = mxArray_p
_libmx.mxCreateUninitNumericMatrix_800.argtypes = [
    c_size_t, c_size_t, c_int, c_int]
_libmx.mxCreateUninitNumericArray_800.restype = mxArray_p
_libmx.mxCreateUninitNumericArray_800.argtypes = [
    c_size_t, POINTER(c_size_t), c_int, c_int]
_libmx.mxSetN_800.argtypes = [mxArray_p, c_size_t]
_libmx.mxSetDimensions_800.restype = c_int
_libmx.mxSetDimensions_800.argtypes = [mxArray_p, POINTER(c_size_t), c_size_t]
_libmx.mxDestroyArray_800.argtypes = [mxArray_p]
_libmx.mxCreateNumericArray_800.restype = mxArray_p
_libmx.mxCreateNumericArray_800.argtypes = [
    c_size_t, POINTER(c_size_t), c_int, c_int]
_libmx.mxCreateCharArray_800.restype = mxArray_p
_libmx.mxCreateCharArray_800.argtypes = [c_size_t, POINTER(c_size_t)]
_libmx.mxCreateDoubleMatrix_800.restype = mxArray_p
_libmx.mxCreateDoubleMatrix_800.argtypes = [c_size_t, c_size_t, c_int]
_libmx.mxGetLogicals_800.restype = POINTER(c_bool)
_libmx.mxGetLogicals_800.argtypes = [mxArray_p]
_libmx.mxCreateLogicalArray_800.restype = mxArray_p
_libmx.mxCreateLogicalArray_800.argtypes = [c_size_t, POINTER(c_size_t)]
_libmx.mxCreateLogicalMatrix_800.restype = mxArray_p
_libmx.mxCreateLogicalMatrix_800.argtypes = [c_size_t, c_size_t]
_libmx.mxCreateLogicalScalar_800.restype = mxArray_p
_libmx.mxCreateLogicalScalar_800.argtypes = [c_bool]
_libmx.mxIsLogicalScalar_800.restype = c_bool
_libmx.mxIsLogicalScalar_800.argtypes = [mxArray_p]
_libmx.mxIsLogicalScalarTrue_800.restype = c_bool
_libmx.mxIsLogicalScalarTrue_800.argtypes = [mxArray_p]
_libmx.mxCreateDoubleScalar_800.restype = mxArray_p
_libmx.mxCreateDoubleScalar_800.argtypes = [c_double]
_libmx.mxCreateSparse_800.restype = mxArray_p
_libmx.mxCreateSparse_800.argtypes = [c_size_t, c_size_t, c_size_t, c_int]
_libmx.mxCreateSparseLogicalMatrix_800.restype = mxArray_p
_libmx.mxCreateSparseLogicalMatrix_800.argtypes = [
    c_size_t, c_size_t, c_size_t]
_libmx.mxGetNChars_800.argtypes = [mxArray_p, c_char_p, c_size_t]
_libmx.mxGetString_800.restype = c_int
_libmx.mxGetString_800.argtypes = [mxArray_p, c_char_p, c_size_t]
_libmx.mxArrayToString_800.restype = c_char_p
_libmx.mxArrayToString_800.argtypes = [mxArray_p]
_libmx.mxArrayToUTF8String_800.restype = c_char_p
_libmx.mxArrayToUTF8String_800.argtypes = [mxArray_p]
_libmx.mxCreateStringFromNChars_800.restype = mxArray_p
_libmx.mxCreateStringFromNChars_800.argtypes = [c_char_p, c_size_t]
_libmx.mxCreateString_800.restype = mxArray_p
_libmx.mxCreateString_800.argtypes = [c_char_p]
_libmx.mxCreateCharMatrixFromStrings_800.restype = mxArray_p
_libmx.mxCreateCharMatrixFromStrings_800.argtypes = [
    c_size_t, POINTER(c_char_p)]
_libmx.mxCreateCellMatrix_800.restype = mxArray_p
_libmx.mxCreateCellMatrix_800.argtypes = [c_size_t, c_size_t]
_libmx.mxCreateCellArray_800.restype = mxArray_p
_libmx.mxCreateCellArray_800.argtypes = [c_size_t, POINTER(c_size_t)]
_libmx.mxCreateStructMatrix_800.restype = mxArray_p
_libmx.mxCreateStructMatrix_800.argtypes = [
    c_size_t, c_size_t, c_int, POINTER(c_char_p)]
_libmx.mxCreateStructArray_800.restype = mxArray_p
_libmx.mxCreateStructArray_800.argtypes = [
    c_size_t, POINTER(c_size_t), c_int, POINTER(c_char_p)]
_libmx.mxDuplicateArray_800.restype = mxArray_p
_libmx.mxDuplicateArray_800.argtypes = [mxArray_p]
_libmx.mxSetClassName_800.restype = c_int
_libmx.mxSetClassName_800.argtypes = [mxArray_p, c_char_p]
_libmx.mxAddField_800.restype = c_int
_libmx.mxAddField_800.argtypes = [mxArray_p, c_char_p]
_libmx.mxRemoveField_800.argtypes = [mxArray_p, c_int]
_libmx.mxGetEps_800.restype = c_double
_libmx.mxGetInf_800.restype = c_double
_libmx.mxGetNaN_800.restype = c_double
_libmx.mxIsFinite_800.restype = c_bool
_libmx.mxIsFinite_800.argtypes = [c_double]
_libmx.mxIsInf_800.restype = c_bool
_libmx.mxIsInf_800.argtypes = [c_double]
_libmx.mxIsNaN_800.restype = c_bool
_libmx.mxIsNaN_800.argtypes = [c_double]

_libmx.mxGetDoubles_800.restype = POINTER(c_double)
_libmx.mxGetDoubles_800.argtypes = [mxArray_p]
_libmx.mxGetSingles_800.restype = POINTER(c_float)
_libmx.mxGetSingles_800.argtypes = [mxArray_p]
_libmx.mxGetInt8s_800.restype = POINTER(c_int8)
_libmx.mxGetInt8s_800.argtypes = [mxArray_p]
_libmx.mxGetUint8s_800.restype = POINTER(c_uint8)
_libmx.mxGetUint8s_800.argtypes = [mxArray_p]
_libmx.mxGetInt16s_800.restype = POINTER(c_int16)
_libmx.mxGetInt16s_800.argtypes = [mxArray_p]
_libmx.mxGetUint16s_800.restype = POINTER(c_uint16)
_libmx.mxGetUint16s_800.argtypes = [mxArray_p]
_libmx.mxGetInt32s_800.restype = POINTER(c_int32)
_libmx.mxGetInt32s_800.argtypes = [mxArray_p]
_libmx.mxGetUint32s_800.restype = POINTER(c_uint32)
_libmx.mxGetUint32s_800.argtypes = [mxArray_p]
_libmx.mxGetInt64s_800.restype = POINTER(c_int64)
_libmx.mxGetInt64s_800.argtypes = [mxArray_p]
_libmx.mxGetUint64s_800.restype = POINTER(c_uint64)
_libmx.mxGetUint64s_800.argtypes = [mxArray_p]


class Complex64(Structure):
    _fields_ = [("real", c_double), ("imag", c_double)]


class Complex32(Structure):
    _fields_ = [("real", c_float), ("imag", c_float)]


class ComplexI8(Structure):
    _fields_ = [("real", c_int8), ("imag", c_int8)]


class ComplexU8(Structure):
    _fields_ = [("real", c_uint8), ("imag", c_uint8)]


class ComplexI16(Structure):
    _fields_ = [("real", c_int16), ("imag", c_int16)]


class ComplexU16(Structure):
    _fields_ = [("real", c_uint16), ("imag", c_uint16)]


class ComplexI32(Structure):
    _fields_ = [("real", c_int32), ("imag", c_int32)]


class ComplexU32(Structure):
    _fields_ = [("real", c_uint32), ("imag", c_uint32)]


class ComplexI64(Structure):
    _fields_ = [("real", c_int64), ("imag", c_int64)]


class ComplexU64(Structure):
    _fields_ = [("real", c_uint64), ("imag", c_uint64)]


_libmx.mxGetComplexDoubles_800.restype = POINTER(Complex64)
_libmx.mxGetComplexDoubles_800.argtypes = [mxArray_p]
_libmx.mxGetComplexSingles_800.restype = POINTER(Complex32)
_libmx.mxGetComplexSingles_800.argtypes = [mxArray_p]
_libmx.mxGetComplexInt8s_800.restype = POINTER(ComplexI8)
_libmx.mxGetComplexInt8s_800.argtypes = [mxArray_p]
_libmx.mxGetComplexUint8s_800.restype = POINTER(ComplexU8)
_libmx.mxGetComplexUint8s_800.argtypes = [mxArray_p]
_libmx.mxGetComplexInt16s_800.restype = POINTER(ComplexI16)
_libmx.mxGetComplexInt16s_800.argtypes = [mxArray_p]
_libmx.mxGetComplexUint16s_800.restype = POINTER(ComplexU16)
_libmx.mxGetComplexUint16s_800.argtypes = [mxArray_p]
_libmx.mxGetComplexInt32s_800.restype = POINTER(ComplexI32)
_libmx.mxGetComplexInt32s_800.argtypes = [mxArray_p]
_libmx.mxGetComplexUint32s_800.restype = POINTER(ComplexU32)
_libmx.mxGetComplexUint32s_800.argtypes = [mxArray_p]
_libmx.mxGetComplexInt64s_800.restype = POINTER(ComplexI64)
_libmx.mxGetComplexInt64s_800.argtypes = [mxArray_p]
_libmx.mxGetComplexUint64s_800.restype = POINTER(ComplexU64)
_libmx.mxGetComplexUint64s_800.argtypes = [mxArray_p]


class libMATException(Exception):
    pass


class InvalidMATFile(libMATException):
    def __init__(self, *args):
        if len(args):
            super().__init__(self, *args)
        else:
            super().__init__(self, "Specified file is not a valid Matlab MAT file.")


class InvalidMATVariable(libMATException):
    def __init__(self, *args):
        if len(args):
            super().__init__(self, *args)
        else:
            super().__init__(self, "Specified variable is not found in this  Matlab MAT file.")


class NoShallowCopy(libMATException):
    def __init__(self, *args):
        if len(args):
            super().__init__(self, *args)
        else:
            super().__init__(self, "Shallow copy is not allowed. Always use deep copy.")


class InfoOnlyArray(libMATException):
    def __init__(self, *args):
        if len(args):
            super().__init__(self, *args)
        else:
            super().__init__(self, "This matlab_array object does not contain data.")


def make_nd_array(c_pointer, size, shape, dtype, order='C'):
    arr_size = size * np.dtype(dtype).itemsize
    buf_from_mem = pythonapi.PyMemoryView_FromMemory
    buf_from_mem.restype = py_object
    buf_from_mem.argtypes = (c_void_p, c_int, c_int)
    buffer = buf_from_mem(c_pointer, arr_size, 0x100)
    arr = np.ndarray(shape, dtype, buffer, order=order)
    return arr


class matlab_array:
    def __init__(self, mxSrc, infoonly=False, destroy=True):
        self._pm = mxSrc
        self._infoonly = infoonly
        self._destroy = destroy

    def __del__(self):
        if self._destroy:
            _libmx.mxDestroyArray_800(self._pm)

    def __bool__(self):
        return not _libmx.mxIsEmpty_800(self._pm) or (_libmx.mxIsLogicalScalar_800(self._pm) and not _libmx.mxIsLogicalScalarTrue_800(self._pm))

    def __copy__(self):
        raise NoShallowCopy()

    def __deepcopy__(self, memo):
        return matlab_array(_libmx.mxDuplicateArray_800(self._pm), self._infoonly)

    def data(self):
        if self._infoonly:
            raise InfoOnlyArray()

        sz = self.size()
        dims = self.shape()

        def to_nd_array(c_pointer, dtype): return make_nd_array(
            c_pointer, sz, dims, dtype)

        if _libmx.mxIsChar_800(self._pm):
            if sz == 0:
                return ''
            elif len(dims) == 2 and dims[0] == 1:  # single string
                return cast(_libmx.mxGetChars_800(self._pm), POINTER(c_wchar * sz)).contents.value
            else:  # array of characters
                return to_nd_array(_libmx.mxGetChars_800(self._pm), np.char.string_)
        elif _libmx.mxIsStruct_800(self._pm):
            nfields = _libmx.mxGetNumberOfFields_800(self._pm)
            if sz == 0:  # create empty dictionary
                return dict()
            elif sz == 1:  # create dictionary
                return dict([(_libmx.mxGetFieldNameByNumber_800(self._pm, i).decode('utf-8'), matlab_array(_libmx.mxGetFieldByNumber_800(self._pm, 0, i), False, False)) for i in range(nfields)])
            else:
                return np.fromfunction(lambda i:  matlab_array(_libmx.mxGetFieldByNumber_800(self._pm, 0, i), False, False), (sz,),
                                       dtype=[(_libmx.mxGetFieldNameByNumber_800(self._pm, i).decode('utf-8'), matlab_array) for i in range(nfields)]).reshape(dims)
        elif _libmx.mxIsEmpty_800(self._pm):
            return None
        elif _libmx.mxIsCell_800(self._pm):  # create ndarray of matlab_arrays
            if sz == 1:
                return matlab_array(_libmx.mxGetCell_800(self._pm, 0), False, False)
            else:
                return np.fromfunction(lambda i: matlab_array(_libmx.mxGetCell_800(self._pm, i), False, False), (sz,),
                                       dtype=matlab_array).reshape(dims)
        elif _libmx.mxIsLogical_800(self._pm):
            if sz == 1:
                return _libmx.mxIsLogicalScalarTrue_800(self._pm).value
            else:
                return to_nd_array(_libmx.mxGetLogicals_800(self._pm), np.bool)
        else:  # numeric
            iscplx = _libmx.mxIsComplex_800(self._pm)

            cfgs = {0: {'istype': _libmx.mxIsDouble_800, 'getdata': _libmx.mxGetDoubles_800, 'getcdata': _libmx.mxGetComplexDoubles_800, 'type': np.float64, 'ctype': np.complex128},
                    1: {'istype': _libmx.mxIsSingle_800, 'getdata': _libmx.mxGetSingles_800, 'getcdata': _libmx.mxGetComplexSingles_800, 'type': np.float32, 'ctype': np.complex64},
                    2: {'istype': _libmx.mxIsInt8_800, 'getdata': _libmx.mxGetInt8s_800, 'getcdata': _libmx.mxGetComplexInt8s_800, 'type': np.int8, 'ctype': np.dtype([('real', np.int8), ('imag', np.int8)])},
                    3: {'istype': _libmx.mxIsUint8_800, 'getdata': _libmx.mxGetUint8s_800, 'getcdata': _libmx.mxGetComplexUint8s_800, 'type': np.uint8, 'ctype': np.dtype([('real', np.uint8), ('imag', np.uint8)])},
                    4: {'istype': _libmx.mxIsInt16_800, 'getdata': _libmx.mxGetInt16s_800, 'getcdata': _libmx.mxGetComplexInt16s_800, 'type': np.int16, 'ctype': np.dtype([('real', np.int16), ('imag', np.int16)])},
                    5: {'istype': _libmx.mxIsUint16_800, 'getdata': _libmx.mxGetUint16s_800, 'getcdata': _libmx.mxGetComplexUint16s_800, 'type': np.uint16, 'ctype': np.dtype([('real', np.uint16), ('imag', np.uint16)])},
                    6: {'istype': _libmx.mxIsInt32_800, 'getdata': _libmx.mxGetInt32s_800, 'getcdata': _libmx.mxGetComplexInt32s_800, 'type': np.int32, 'ctype': np.dtype([('real', np.int32), ('imag', np.int32)])},
                    7: {'istype': _libmx.mxIsUint32_800, 'getdata': _libmx.mxGetUint32s_800, 'getcdata': _libmx.mxGetComplexUint32s_800, 'type': np.uint32, 'ctype': np.dtype([('real', np.uint32), ('imag', np.uint32)])},
                    8: {'istype': _libmx.mxIsInt64_800, 'getdata': _libmx.mxGetInt64s_800, 'getcdata': _libmx.mxGetComplexInt64s_800, 'type': np.int64, 'ctype': np.dtype([('real', np.int64), ('imag', np.int64)])},
                    9: {'istype': _libmx.mxIsUint64_800, 'getdata': _libmx.mxGetUint64s_800, 'getcdata': _libmx.mxGetComplexUint64s_800, 'type': np.uint64, 'ctype': np.dtype([('real', np.uint64), ('imag', np.uint64)])},
                    }

            index = next((i for i in range(len(cfgs))
                          if cfgs[i]['istype'](self._pm)), len(cfgs))
            if index < len(cfgs):
                cfg = cfgs[index]
                pdata = (cfg['getcdata'](self._pm)
                         if iscplx else cfg['getdata'](self._pm))
                if sz == 1:
                    return pdata[0]
                return to_nd_array(pdata, (cfg['ctype'] if iscplx else cfg['type']))
            else:
                raise Exception("Unsupported data type")

    def size(self):
        return _libmx.mxGetNumberOfElements_800(self._pm)

    def shape(self):
        ndims = _libmx.mxGetNumberOfDimensions_800(self._pm)
        dims = _libmx.mxGetDimensions_800(self._pm)
        rval = ()
        for i in range(ndims):
            rval += (dims[i],)
        return rval

    def mtype(self):
        if _libmx.mxGetClassID_800(self._pm) == 0:
            return 'class'
        else:
            return _libmx.mxGetClassName_800(self._pm).decode('utf-8')


class matfile:

    def __init__(self, path, mode='r'):
        if not os.path.exists(path):
            path = os.path.join(sys.path[0],path)
        self._mfp = _libmat.matOpen_800(
            path.encode('utf-8'), mode.encode('utf-8'))
        if not self._mfp:
            raise InvalidMATFile()
        self.path = path
        self._mode = mode

    def __del__(self):
        if self._mfp:
            _libmat.matClose_800(self._mfp)

    def __copy__(self):
        raise NoShallowCopy()

    def __deepcopy__(self, memo):
        return matfile(self.path, self._mode)

    def __getitem__(self, key):
        return self.getVariable(key)

    def __setitem__(self, key, val):
        self.setVariable(key, val)

    def __delitem__(self, key):
        return self.deleteVariable(key)
    
    def __len__(self):
        return len(self.getDir())

    def getVariable(self, varname):  # Array from MAT-file
        array = _libmat.matGetVariable_800(self._mfp, varname.encode('utf-8'))
        if array:
            return matlab_array(array)
        else:
            raise InvalidMATVariable()

    def getVariableInfo(self, varname):  # Array header information only
        array = _libmat.matGetVariableInfo_800(
            self._mfp, varname.encode('utf-8'))
        if array:
            return matlab_array(array, True)
        else:
            raise InvalidMATVariable()

    def getNextVariable(self):  # Next array in MAT-file
        varname = POINTER(c_char)()
        array = _libmat.matGetNextVariable_800(self._mfp, byref(varname))
        if array:
            return (cast(varname, c_char_p).value.decode('utf-8'), matlab_array(array))
        else:
            return ()

    def getNextVariableInfo(self):  # Array header information only
        varname = POINTER(c_char)()
        array = _libmat.matGetNextVariableInfo_800(self._mfp, byref(varname))
        if array:
            return (cast(varname, c_char_p).value.decode('utf-8'), matlab_array(array, True))
        else:
            return ()

    def putVariable(self, varname, vardata):  # Array to MAT-file
        return _libmat.matPutVariable_800(self._mfp, varname.encode('utf-8'), vardata._pm)

    # Array to MAT-file as originating from global workspace
    def putVariableAsGlobal(self, varname, vardata):
        return _libmat.matPutVariableAsGlobal_800(self._mfp, varname.encode('utf-8'), vardata._pm)

    def deleteVariable(self, varname):  # Delete array from MAT-file
        return _libmat.matDeleteVariable_800(self._mfp, varname.encode('utf-8'))

    def getDir(self):  # List of variables in MAT-file
        numvars = c_int()
        pvarnames = _libmat.matGetDir_800(self._mfp, byref(numvars))
        varlist = []
        for i in range(numvars.value):
            varlist.append(pvarnames[i].decode("utf-8"))
        _libmx.mxFree_800(pvarnames)
        return varlist

    def getErrno(self):  # Error codes for MAT-file API
        return _libmat.matGetErrno_800(self._mfp)
