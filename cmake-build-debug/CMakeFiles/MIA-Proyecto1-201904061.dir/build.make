# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.21

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
CMAKE_COMMAND = /snap/clion/175/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /snap/clion/175/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jose/Desktop/MIA-Proyecto1-201904061

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/MIA-Proyecto1-201904061.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/MIA-Proyecto1-201904061.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make

CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.o: ../src/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/main.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/main.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/main.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.o: ../src/analizador/scanner.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/analizador/scanner.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/analizador/scanner.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/analizador/scanner.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.o: ../src/analizador/parser.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/analizador/parser.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/analizador/parser.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/analizador/parser.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.o: ../src/comandos/Command.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Command.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Command.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Command.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.o: ../src/comandos/Mkdisk.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkdisk.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkdisk.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkdisk.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.o: ../src/comandos/Param.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Param.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Param.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Param.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.o: ../src/comandos/Rmdisk.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Rmdisk.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Rmdisk.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Rmdisk.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.o: ../src/comandos/Fdisk.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Fdisk.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Fdisk.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Fdisk.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.o: ../src/comandos/Mount.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mount.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mount.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mount.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.o: ../src/Entidades/Disco.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/Entidades/Disco.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/Entidades/Disco.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/Entidades/Disco.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.o: ../src/comandos/Umount.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Umount.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Umount.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Umount.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.o: ../src/comandos/Mkfs.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_12) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkfs.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkfs.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkfs.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.o: ../src/comandos/Rep.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_13) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Rep.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Rep.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Rep.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.o: ../src/comandos/Exec.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_14) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Exec.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Exec.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Exec.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.o: ../src/comandos/Usuarios/Login.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_15) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Usuarios/Login.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Usuarios/Login.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Usuarios/Login.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.o: ../src/comandos/Archivos/MkFile.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_16) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Archivos/MkFile.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Archivos/MkFile.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Archivos/MkFile.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.s

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.o: CMakeFiles/MIA-Proyecto1-201904061.dir/flags.make
CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.o: ../src/comandos/Mkdir.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_17) "Building CXX object CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.o -c /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkdir.cpp

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkdir.cpp > CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.i

CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jose/Desktop/MIA-Proyecto1-201904061/src/comandos/Mkdir.cpp -o CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.s

# Object files for target MIA-Proyecto1-201904061
MIA__Proyecto1__201904061_OBJECTS = \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.o" \
"CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.o"

# External object files for target MIA-Proyecto1-201904061
MIA__Proyecto1__201904061_EXTERNAL_OBJECTS =

MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/main.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/scanner.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/analizador/parser.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Command.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdisk.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Param.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rmdisk.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Fdisk.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mount.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/Entidades/Disco.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Umount.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkfs.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Rep.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Exec.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Usuarios/Login.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Archivos/MkFile.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/src/comandos/Mkdir.cpp.o
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/build.make
MIA-Proyecto1-201904061: CMakeFiles/MIA-Proyecto1-201904061.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_18) "Linking CXX executable MIA-Proyecto1-201904061"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MIA-Proyecto1-201904061.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/MIA-Proyecto1-201904061.dir/build: MIA-Proyecto1-201904061
.PHONY : CMakeFiles/MIA-Proyecto1-201904061.dir/build

CMakeFiles/MIA-Proyecto1-201904061.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/MIA-Proyecto1-201904061.dir/cmake_clean.cmake
.PHONY : CMakeFiles/MIA-Proyecto1-201904061.dir/clean

CMakeFiles/MIA-Proyecto1-201904061.dir/depend:
	cd /home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jose/Desktop/MIA-Proyecto1-201904061 /home/jose/Desktop/MIA-Proyecto1-201904061 /home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug /home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug /home/jose/Desktop/MIA-Proyecto1-201904061/cmake-build-debug/CMakeFiles/MIA-Proyecto1-201904061.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/MIA-Proyecto1-201904061.dir/depend

