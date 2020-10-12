cmake_minimum_required(VERSION 3.10)

project(CASqrt)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
add_subdirectory(cellart)
