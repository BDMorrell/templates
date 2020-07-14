cmake_minimum_required(VERSION 3.14)
project(>>PROJNAME<<)

# Requirements
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Configuration
option(BUILD_TESTS "Build included tests" ON)

# Code generation
# > configure_file("file.h.in" "where.h")

# Source compiling
add_subdirectory(src)

# Test code
if(BUILD_TESTS)
  include(CTest)
  add_subdirectory(test)
endif()

