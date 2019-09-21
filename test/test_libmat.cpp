#include <iostream>
#include <mat.h>
#include <string>
#include <vector>
#include <limits>

void main()
{
  std::string filename = "D:\\Users\\tikuma\\Documents\\Research\\hsvanalysis-"
                         "py\\test\\mknpnl_05.had";

  MATFile *FILE = matOpen(filename.c_str(), "r");
  if (!FILE)
  {
    std::cout << "Failed to open " << filename << std::endl;
    return;
  }
  std::cout << "Opened " << filename << std::endl;

  // List of variables in MAT-file
  int numvars;
  char **varlist = matGetDir(FILE, &numvars);
  std::cout << "There are " << numvars << " variables in this MAT file."
            << std::endl;
  for (int i = 0; i < numvars; ++i)
  {
    mxArray *array = matGetVariableInfo(FILE, varlist[i]);
    mwSize ndims = mxGetNumberOfDimensions(array);
    const size_t *dims = mxGetDimensions(array);
    std::cout << "  " << i << " " << varlist[i] << " [" << dims[0];
    for (int i = 1; i < ndims; ++i) std::cout << "," << dims[i];
    std::cout << "]" << std::endl;
  }
  mxFree(varlist);

  // matGetVariable	Array from MAT-file
  // matGetVariableInfo	Array header information only
  // matGetNextVariable	Next array in MAT-file
  // matGetNextVariableInfo	Array header information only

  matClose(FILE);

  std::cout << "Maximum size allowed: " << std::numeric_limits<size_t>::max() << std::endl;
  std::cout << "Maximum uint32: " << std::numeric_limits<uint32_t>::max() << std::endl;

  for (int i = 0; i<20; ++i)
    std::cout << "mxClassID=" << i

}
