# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/build

# Include any dependencies generated for this target.
include CMakeFiles/embed_python_class.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/embed_python_class.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/embed_python_class.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/embed_python_class.dir/flags.make

CMakeFiles/embed_python_class.dir/main.cpp.o: CMakeFiles/embed_python_class.dir/flags.make
CMakeFiles/embed_python_class.dir/main.cpp.o: ../main.cpp
CMakeFiles/embed_python_class.dir/main.cpp.o: CMakeFiles/embed_python_class.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/embed_python_class.dir/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/embed_python_class.dir/main.cpp.o -MF CMakeFiles/embed_python_class.dir/main.cpp.o.d -o CMakeFiles/embed_python_class.dir/main.cpp.o -c /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/main.cpp

CMakeFiles/embed_python_class.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/embed_python_class.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/main.cpp > CMakeFiles/embed_python_class.dir/main.cpp.i

CMakeFiles/embed_python_class.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/embed_python_class.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/main.cpp -o CMakeFiles/embed_python_class.dir/main.cpp.s

# Object files for target embed_python_class
embed_python_class_OBJECTS = \
"CMakeFiles/embed_python_class.dir/main.cpp.o"

# External object files for target embed_python_class
embed_python_class_EXTERNAL_OBJECTS =

embed_python_class: CMakeFiles/embed_python_class.dir/main.cpp.o
embed_python_class: CMakeFiles/embed_python_class.dir/build.make
embed_python_class: /usr/lib/x86_64-linux-gnu/libpython3.10.so
embed_python_class: CMakeFiles/embed_python_class.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable embed_python_class"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/embed_python_class.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/embed_python_class.dir/build: embed_python_class
.PHONY : CMakeFiles/embed_python_class.dir/build

CMakeFiles/embed_python_class.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/embed_python_class.dir/cmake_clean.cmake
.PHONY : CMakeFiles/embed_python_class.dir/clean

CMakeFiles/embed_python_class.dir/depend:
	cd /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/build /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/build /home/nathan.johnson/pybind_binding_python_and_cpp/first_attempt/build/CMakeFiles/embed_python_class.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/embed_python_class.dir/depend
