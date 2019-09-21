cmake_minimum_required(VERSION 3.10) 
# for FindMatlab support (may require a later version to detect the latest Matlab release)

project (ctest)

find_package(Matlab REQUIRED COMPONENTS MAT_LIBRARY)

add_executable(test_libmat test_libmat.cpp)
target_include_directories(test_libmat PUBLIC ${Matlab_INCLUDE_DIRS})
target_link_libraries(test_libmat PUBLIC ${Matlab_MAT_LIBRARY} ${Matlab_MX_LIBRARY})

install(FILES test_libmat.bat DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
