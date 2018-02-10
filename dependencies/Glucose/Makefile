################################################################################
# This make file serves the purpose of compiling and patching minisat for your
# platform.
#
# This file is part of the pynusmv distribution. As such it is licensed to you
# under the term of the LGPLv2. For more information regarding the legal aspect
# of this licensing, please refer to the full text of the license on the free
# software foundation website.
#
# Author: V.Feyens <victor.feyens[at] student.uclouvain.be>
################################################################################

# This target goes through all the steps required to compile MiniSat.
all: glucose.built

# This target wipes off everything that has been unpacked and built.
clean:
	rm -rf glucose-syrup-4.1
	rm glucose.unpacked
	rm glucose.patched

# This target just unpacks the zip containing minisat
glucose.unpacked:
	tar xzvf glucose-syrup-4.1.tgz #unzip glucose-syrup-4.1.zip
	touch glucose.unpacked

# patch glucose source code
glucose.patched: glucose.unpacked
	patch -p0 -N < solver.patch #Random seed functionality for NUSMV
	patch -p0 -N < glucose_wrappers.patch #C wrappers + Glucose Makefile
	# patch -p0 -N < nusmv.patch #depends.mk patch, seems unnecessary, to verify later
    # Patch the makefiles to produce position independent code
    # This is necessary to create a sharedlib containing the minisat symbols
	patch -p0 -N < makefiles.patch #-fPic cflag : necessary?
	touch glucose.patched

# This target proceeds to the build (proper) of the glucose codebase
glucose.built: glucose.patched
	make -C glucose-syrup-4.1
	
