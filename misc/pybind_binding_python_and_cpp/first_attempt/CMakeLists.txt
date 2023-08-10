cmake_minimum_required(VERSION 3.12)
project(embed_python_class)

set(CMAKE_CXX_STANDARD 14)

# Find pybind11 package
set(CMAKE_PREFIX_PATH "/home/nathan.johnson/.local/lib/python3.10/site-packages/pybind11" ${CMAKE_PREFIX_PATH})
find_package(pybind11 REQUIRED)

# Add the C++ executable
add_executable(embed_python_class main.cpp)

# Link the executable with pybind11
target_link_libraries(embed_python_class PRIVATE pybind11::embed)

